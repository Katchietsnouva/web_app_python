# I want to use python and selenium to send some text and images to a group of my contacts. I already have a working code for sending the text, but have failed to find a way to send the images. I'm particularly stuck at selecting the image.
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
import time
import pyautogui

service = Service(log_path = "log.log")

driver = webdriver.Firefox(service = service)

driver.get("https://web.whatsapp.com")

print("Scan QR Code, And then Enter")
input()
print("Logged In")

contacts = ["John Doe", "Mary Jane"]

text = """This text works"""

file_path = "/home/xyz/Downloads/abcdef.jpeg"

for contact in contacts:

    input_box_search = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/div[2]/div/div[1]")

    input_box_search.click()
    time.sleep(2)

    for i in contact:
        input_box_search.send_keys(i)
        time.sleep(0.05)

    selected_contact = driver.find_element(By.XPATH, "//span[@title='"+contact+"']")
    selected_contact.click()

    inp_xpath = "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]"
    input_box = driver.find_element(By.XPATH, inp_xpath)
    time.sleep(2)

    input_box.click()

    for i in text:
        input_box.send_keys(i)
        time.sleep(0.05)

    input_box.send_keys(Keys.ENTER)

    time.sleep(2)

    add_sign = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div")
    add_sign.click()
    time.sleep(1)

    photo_icon = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/span")
    photo_icon.click()

    ### This one fails. So does keyboard
    pyautogui.typewrite(file_path)

    send_icon = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div")
    send_icon.click()

driver.quit()