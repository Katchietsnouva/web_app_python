
# Automated Testing for Dynamic Content:

# Create a Selenium script to test a webpage with dynamically changing content.
# Use WebDriverWait to handle elements that load asynchronously.
# Implement assertions to validate that dynamic content updates as expected.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver
driver = webdriver.Chrome()
driver.get("https://nouvaneons.netlify.app/")

# Wait for dynamic content to load
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "your_dynamic_element_id"))
)

# Perform assertions on the dynamic content
assert "Expected Text" in element.text

# Close the browser
driver.quit()
