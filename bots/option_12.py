# 12. Headless Browsing for Enhanced Performance:

from selenium import webdriver

# Set up headless WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# Perform tasks without a visible browser
# ...

# Close the headless browser
driver.quit()
