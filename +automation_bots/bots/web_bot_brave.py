
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# # Path to the Brave browser executable
# brave_path = 'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'  # Replace with the actual path

# # Set Brave browser options
# brave_options = webdriver.ChromeOptions()
# brave_options.binary_location = brave_path  # Set the binary location for Brave

# # Create a new service and provide the path to the executable
# service = Service('C:\Desktop\django_tut\web_app_python\chromedriver-win64\chromedriver.exe')  # Replace with the actual path to chromedriver executable

# # Instantiate the Brave browser
# driver = webdriver.Chrome(service=service, options=brave_options)

# # Navigate to a website
# driver.get("https://example.com")

# # Perform interactions or assertions as needed

# # Close the browser window
# driver.quit()




# from selenium import webdriver

# # Path to the Brave browser executable
# brave_path = 'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'  # Replace with the actual path

# # Set Brave browser options
# brave_options = webdriver.ChromeOptions()
# brave_options.binary_location = brave_path  # Set the binary location for Brave

# # Path to the ChromeDriver executable
# chrome_driver_path = 'C:\Desktop\django_tut\web_app_python\chromedriver-win64\chromedriver.exe'  # Replace with the actual path to chromedriver executable

# # Instantiate the Brave browser with ChromeDriver
# driver = webdriver.Chrome(executable_path=chrome_driver_path, options=brave_options)








# from selenium import webdriver

# # Path to the Brave browser executable
# brave_path = 'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'  # Replace with the actual path

# # Set Brave browser options
# brave_options = webdriver.ChromeOptions()
# brave_options.binary_location = brave_path  # Set the binary location for Brave

# # Path to the ChromeDriver executable
# chrome_driver_path = 'C:\Desktop\django_tut\web_app_python\chromedriver-win64\chromedriver.exe'  # Replace with the actual path to chromedriver executable

# # Instantiate the Brave browser with ChromeDriver
# driver = webdriver.Chrome(executable_path=chrome_driver_path, options=brave_options)

# # Navigate to a website
# driver.get("https://example.com")

# # Perform interactions or assertions as needed

# # Close the browser window
# driver.quit()







# from selenium import webdriver

# # Path to the Brave browser executable
# # brave_path = 'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'  # Replace with the actual path
# brave_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'

# # Set Brave browser options
# brave_options = webdriver.ChromeOptions()
# brave_options.binary_location = brave_path  # Set the binary location for Brave

# # Instantiate the Brave browser with ChromeDriver
# # driver = webdriver.Chrome(options=brave_options)
# driver = webdriver.Chrome(executable_path=brave_path)

# # Navigate to a website
# driver.get("https://example.com")

# # Perform interactions or assertions as needed

# # Close the browser window
# driver.quit()



import time
from selenium import webdriver

# Path to the Brave browser executable
brave_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'

# Set Brave browser options
brave_options = webdriver.ChromeOptions()
brave_options.binary_location = brave_path  # Set the binary location for Brave

# Instantiate the ChromeDriver with Brave options
driver = webdriver.Chrome(options=brave_options)

# Navigate to a website
driver.get("https://nouvaneons.netlify.app/")

# Perform interactions or assertions as needed
# Add a delay to keep the browser window open for 10 seconds
time.sleep(1000)

# Close the browser window
driver.quit()
