import time
from selenium import webdriver
from bs4 import BeautifulSoup

# Path to the Brave browser executable
brave_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'

# Set Brave browser options
brave_options = webdriver.ChromeOptions()
brave_options.binary_location = brave_path  # Set the binary location for Brave

# Instantiate the ChromeDriver with Brave options
driver = webdriver.Chrome(options=brave_options)

# Navigate to a website
driver.get("https://nouvaneons.netlify.app/")

# Wait for some time to ensure the page is loaded (adjust as needed)
time.sleep(20)

# Get the page source
page_source = driver.page_source

# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(page_source, 'html.parser')

# Extract information from the page using BeautifulSoup
# (Replace this with your actual scraping logic)
title = soup.title.text
print("Page Title:", title)

# Close the browser window
driver.quit()
