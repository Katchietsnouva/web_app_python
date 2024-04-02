# Browser Automation for Social Media:

# Automate actions on social media platforms (e.g., posting, liking, following) using Selenium.
# Be cautious and respectful of the platform's terms of service.

# 7. Price Monitoring on E-commerce Websites:

from selenium import webdriver
import time

# Set up WebDriver
driver = webdriver.Chrome()
driver.get("product_page_url")

# Extract the initial price
initial_price = driver.find_element_by_xpath('//span[@class="price"]')

# Monitor the price over time
while True:
    time.sleep(3600)  # Check every hour
    current_price = driver.find_element_by_xpath('//span[@class="price"]')
    if current_price < initial_price:
        print("Price dropped!")
        # Take action: send notification, etc.

# Close the browser
driver.quit()
