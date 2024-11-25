import requests
from bs4 import BeautifulSoup
import time
import random
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables from .env file
load_dotenv()
PUSHOVER_USER_KEY = os.getenv("PUSHOVER_USER_KEY")  # Your Pushover User Key
PUSHOVER_API_TOKEN = os.getenv("PUSHOVER_API_TOKEN")  # Your Pushover API Token

# URL to monitor
URL = "https://www.findbolig.nu/da-dk/udlejere"

# User-Agent header to mimic a browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

# Function to log errors
def log_error(error_message):
    log_message(error_message, "error_log.txt")

# Function to log messages
def log_message(message, filename=None):
    now = datetime.now()
    log_dir = os.path.join("logs", now.strftime("%Y"), now.strftime("%m"))
    os.makedirs(log_dir, exist_ok=True)
    if filename is None:
        filename = now.strftime("%Y-%m-%d") + ".txt"
    log_file_path = os.path.join(log_dir, filename)
    with open(log_file_path, "a") as log_file:
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {message}\n")
        print(f"Logged message: {message}")

# Function to check occurrences of "lukket" and "åben"
def check_page_content():
    try:
        # Fetch the page
        response = requests.get(URL, headers=HEADERS)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Count occurrences of the words "lukket" and "åben"
        page_text = soup.get_text().lower()
        lukket_count = page_text.count("lukket")
        aaben_count = page_text.count("åben")
        
        # log_message(f"'lukket' found {lukket_count} times.")
        # log_message(f"'åben' found {aaben_count} times.")
        
        # Check both conditions
        lukket_condition = lukket_count != 10
        aaben_condition = aaben_count > 1
        
        return lukket_condition and aaben_condition
    except Exception as e:
        error_message = f"Error while fetching the page: {e}"
        log_error(error_message)  # Log the error
        return None

# Function to send a Pushover notification
def send_pushover_notification():
    try:
        url = "https://api.pushover.net/1/messages.json"
        payload = {
            "token": PUSHOVER_API_TOKEN,
            "user": PUSHOVER_USER_KEY,
            "message": "'lukket' and 'åben' conditions met on the monitored page!",
            "title": "Website Alert",
            "priority": 1,  # High priority
            "sound": "siren"  # Use the 'siren' sound for an alarm
        }
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            log_message("Pushover notification sent.")
        else:
            error_message = f"Failed to send Pushover notification: {response.text}"
            log_error(error_message)  # Log the error
    except Exception as e:
        error_message = f"Error sending Pushover notification: {e}"
        log_error(error_message)  # Log the error

# Main monitoring function
def monitor_page():
    while True:
        status = check_page_content()
        if status is None:
            log_message("Could not check the page. Retrying...")
        elif status:  # If both conditions are met
            send_pushover_notification()
            log_message("Notification sent. Waiting for 15 seconds before resuming monitoring...")
            time.sleep(15)  # Wait for 15 seconds before continuing
        else:
            log_message("Lists are closed.")

        # Wait for a random interval between 5 and 10 seconds
        delay = random.randint(5, 10)
        time.sleep(delay)

# Entry point
if __name__ == "__main__":
    monitor_page()