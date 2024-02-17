# # 3. Screen Capture and Image Recognition:

# import pyautogui

# # Take a screenshot and locate an image on the screen
# screenshot = pyautogui.screenshot()
# location = pyautogui.locateOnScreen('sample.jpg')  # Replace with your image file

# if location:
#     pyautogui.click(location)
# else:
#     print("Image not found on the screen.")


import pyautogui

# Capture a region of the screen
# screenshot = pyautogui.screenshot(region=(100, 100, 300, 300))
screenshot = pyautogui.screenshot(region=(200, 200, 424, 420))  # Replace with your screen resolution

# screenshot = pyautogui.screenshot()
screenshot.save('captured_image.png')

# Locate the captured image on the screen
location = pyautogui.locateOnScreen('captured_image.png')
# location = pyautogui.locateOnScreen('captured_image.png', tolerance=10)

if location:
    pyautogui.click(location)
else:
    print("Image not found on the screen.")
