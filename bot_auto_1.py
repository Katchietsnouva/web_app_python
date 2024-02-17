import pyautogui
import time

# Simulate a test scenario
pyautogui.moveTo(100, 100)  # Move the mouse to (100, 100)
pyautogui.click()  # Click at the current mouse position
pyautogui.typewrite("Hello, PyAutoGUI!")  # Type a message
time.sleep(2)  # Pause for 2 seconds
