--------------------------------------🛒 AliExpress Image Scraper--------------------------------------     

A dedicated Python-based scraper that automatically extracts high-resolution product images from AliExpress product pages. Built with Selenium, it simulates human-like behavior to click image thumbnails, bypass CAPTCHA challenges, and download images into organized folders—ideal for e-commerce automation and competitor analysis.

🧰 Features:

1) 📥 Product Image Download
Extracts and saves all high-resolution product images from AliExpress pages.
2) 🔗 Multiple URL Support
Reads a list of product URLs from a CSV file (aliexpress_products.csv) with a column named url.
3) 🧠 Human-like Browsing
Uses randomized delays and browser flags to reduce bot detection.
4) 🔁 Automated CAPTCHA Detection
Detects and handles Google reCAPTCHA challenges with frame switching.
5) 🖼️ Image Thumbnail Clicking
Automatically clicks all image thumbnails to fetch main image URLs for download.
6) 📂 Structured Folder Output
Each product’s images and URL are saved in their own folder (product_1, product_2, etc.).
7) 📴 Popup Handling
Detects and closes annoying pop-ups automatically for uninterrupted scraping.


🛠️ Technologies Used:

--> Python 3.9+

--> Selenium WebDriver

--> Chrome WebDriver (Headed/Headless)

--> WebDriver Manager

--> Pandas for CSV Handling

--> Requests for Image Downloading

--> XPath / Class Selectors for DOM Targeting


🚀 How It Works:
Reads product URLs from aliexpress_products.csv.
Starts a Chrome browser session with anti-bot flags.
Navigates to each product URL.
Clicks all image thumbnails one by one.
Extracts the full-size image source (src) of each.
Downloads and saves them in structured folders.
Handles reCAPTCHA frames and popups when detected.

📸 Sample Use Case:
Want to extract all images of cabinet knobs or dresses listed on AliExpress?
Just paste their product URLs into the CSV—this script automates the rest!

📩 Hire Me:

Need a custom scraping solution for AliExpress, Amazon, or any other e-commerce platform?

💼 I’m available for freelance projects!

📧 Contact Me:
Email: roohanitech121@gmail.com 

Fiverr: fiverr.com/users/roohullah2020/ 

Let’s automate your next e-commerce scraping project! 🤖✨
