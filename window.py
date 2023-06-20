import time
import pyautogui
import requests
import os
from bs4 import BeautifulSoup
from twilio.rest import Client
# import yagmail
import logging

TWILIO_ACCOUNT_SID = "" # replace with your Account SID 
TWILIO_AUTH_TOKEN = "" # replace with your Auth Token
TWILIO_PHONE_SENDER = "whatsapp:" # replace with the phone number you registered in twilio
TWILIO_PHONE_RECIPIENT = "whatsapp:" # replace with your phone number

new_refresh_image = None

def send_text_alert(alert_str):
    """Sends an SMS text alert."""
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        from_=TWILIO_PHONE_SENDER,
        body=alert_str,
        to=TWILIO_PHONE_RECIPIENT)


def capture_screen():
    """Capture the current screen as an image."""
    left_monitor_width = 1920  # Width of the left monitor
    screenshot = pyautogui.screenshot(region=(0, 0, left_monitor_width, 1080))
    return screenshot

def images_are_equal(image1, image2):
    """Compare two images and return True if they are equal, otherwise False."""
    return image1 == image2

def monitor_screen_changes():
    """Monitor the left screen for changes."""
    previous_image = capture_screen()
    counter = 0

    while True:

        if counter == 1800:
            pyautogui.hotkey('f5')
            print('refresh')
            time.sleep(10)

        current_image = capture_screen()

        if counter == 1800:
            previous_image = current_image
            counter = 0

        if not images_are_equal(previous_image, current_image):
            print("Left screen changed!")
            # Add your desired actions here

        previous_image = current_image
        time.sleep(1)  # Adjust the delay between checks if needed
        counter += 1

# Start monitoring the left screen
monitor_screen_changes()
