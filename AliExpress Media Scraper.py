import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Setup Selenium

def init_driver(headless=False):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--start-maximized")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Close popups
def close_popups(driver):
    try:
        driver.find_element(By.CLASS_NAME, "pop-close-btn").click()
    except:
        pass
    try:
        driver.find_element(By.CLASS_NAME, "Sk1_X._1-SOk").click()
    except:
        pass

# Save image
def download_image(img_url, folder, index):
    try:
        ext = img_url.split('.')[-1].split('?')[0]
        img_data = requests.get(img_url, timeout=10).content
        with open(os.path.join(folder, f'image_{index}.{ext}'), 'wb') as f:
            f.write(img_data)
    except Exception as e:
        print(f"Failed to download image {img_url}: {e}")

# Process a single product URL
def process_product(driver, url, index):
    driver.get(url)
    time.sleep(5)
    
    # handle_captcha(driver)  # Handle CAPTCHA if present
    close_popups(driver)
    time.sleep(2)

    folder_name = f"product_{index}"
    os.makedirs(folder_name, exist_ok=True)

    # Save the product URL
    with open(os.path.join(folder_name, f"product_{index}_url.txt"), 'w') as f:
        f.write(url)

    # Find all thumbnails
    try:
        thumbs_container = driver.find_element(By.CLASS_NAME, "slider--slider--VKj5hty")
        thumbs = thumbs_container.find_elements(By.CLASS_NAME, "slider--img--kD4mIg7")
    except NoSuchElementException:
        print(f"Thumbnail container not found for: {url}")
        return

    for i, thumb in enumerate(thumbs):
        try:
            thumb.click()
            time.sleep(1)

            main_image_div = driver.find_element(By.CLASS_NAME, "magnifier--wrap--qjbuwmt")
            img_tag = main_image_div.find_element(By.TAG_NAME, 'img')
            img_url = img_tag.get_attribute('src')

            if img_url:
                download_image(img_url, folder_name, i + 1)

        except Exception as e:
            print(f"Error clicking/downloading thumbnail {i+1}: {e}")

def process_product(driver, url, index):
    
    driver.get(url)
    time.sleep(3)  # Let the page start loading

    # Inline CAPTCHA click handling
    try:
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        for iframe in iframes:
            if "recaptcha" in iframe.get_attribute("title").lower():
                driver.switch_to.frame(iframe)
                print("Switched to reCAPTCHA iframe")
                try:
                    checkbox = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CLASS_NAME, "recaptcha-checkbox-border"))
                    )
                    checkbox.click()
                    print("CAPTCHA checkbox clicked.")
                    time.sleep(3)  # Let Google verify
                except Exception as inner_e:
                    print("CAPTCHA checkbox not clickable:", inner_e)
                finally:
                    driver.switch_to.default_content()
                break
    except Exception as outer_e:
        print("No CAPTCHA iframe found or error:", outer_e)

    close_popups(driver)
    time.sleep(2)

    folder_name = f"product_{index}"
    os.makedirs(folder_name, exist_ok=True)

    with open(os.path.join(folder_name, f"product_{index}_url.txt"), 'w') as f:
        f.write(url)

    try:
        thumbs_container = driver.find_element(By.CLASS_NAME, "slider--slider--VKj5hty")
        thumbs = thumbs_container.find_elements(By.CLASS_NAME, "slider--img--kD4mIg7")
    except NoSuchElementException:
        print(f"Thumbnail container not found for: {url}")
        return

    for i, thumb in enumerate(thumbs):
        try:
            thumb.click()
            time.sleep(1)
            main_image_div = driver.find_element(By.CLASS_NAME, "magnifier--wrap--qjbuwmt")
            img_tag = main_image_div.find_element(By.TAG_NAME, 'img')
            img_url = img_tag.get_attribute('src')

            if img_url:
                download_image(img_url, folder_name, i + 1)
        except Exception as e:
            print(f"Error clicking/downloading thumbnail {i+1}: {e}")


# Main logic
def main():
    csv_file = "aliexpress_products.csv"
    df = pd.read_csv(csv_file)

    if 'url' not in df.columns:
        print("CSV must have a column named 'url'")
        return

    driver = init_driver(headless=False)

    for idx, row in df.iterrows():
        url = row['url']
        print(f"Processing product {idx+1}: {url}")
        process_product(driver, url, idx + 1)

    driver.quit()
    print("All done.")

if __name__ == "__main__":
    main()
