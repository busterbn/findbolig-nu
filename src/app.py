import requests
from bs4 import BeautifulSoup
import time
import random
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
PUSHOVER_USER_KEY = os.getenv("PUSHOVER_USER_KEY")  # Your Pushover User Key
PUSHOVER_API_TOKEN = os.getenv("PUSHOVER_API_TOKEN")  # Your Pushover API Token
TEST_MODE = os.getenv("TEST_MODE", "False").lower() == "true"  # Enable if TEST_MODE=True in .env or runtime


# URL to monitor
URL = "https://www.findbolig.nu/da-dk/udlejere"

# User-Agent header to mimic a browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

check_count = 0

# Function to check the number of occurrences of "lukket"
def check_if_lukket_appears():
    try:
        # Fetch the page
        response = requests.get(URL, headers=HEADERS)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Count occurrences of the word "lukket"
        page_text = soup.get_text().lower()
        lukket_count = page_text.count("lukket")
        print(f"'lukket' found {lukket_count} times on the page.")  # Log the count
        
        # Return True if it appears exactly 10 times
        return lukket_count == 10
    except Exception as e:
        print(f"Error while fetching the page: {e}")
        return None

# Function to send a Pushover notification
def send_pushover_notification():
    try:
        url = "https://api.pushover.net/1/messages.json"
        payload = {
            "token": PUSHOVER_API_TOKEN,
            "user": PUSHOVER_USER_KEY,
            "message": "'Lukket' no longer appears 10 times on the page. Check the website immediately!",
            "title": "Website Alert",
            "priority": 1,  # High priority
            "sound": "siren"  # Use the 'siren' sound for an alarm
        }
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("Pushover notification sent.")
        else:
            print(f"Failed to send Pushover notification: {response.text}")
    except Exception as e:
        print(f"Error sending Pushover notification: {e}")

# Monitor the page in a loop with random intervals
while True:
    check_count
    check_count += 1  # Increment the counter for each check

    # Test mode: Trigger notification on the 3rd check
    if TEST_MODE and check_count == 2:
        print("Test mode: Sending notification after the 2. check.")
        send_pushover_notification()
        break

    # Check the page normally
    status = check_if_lukket_appears()
    if status is not None:
        if not status:  # If "lukket" does not appear exactly 10 times
            send_pushover_notification()
            break  # Exit the loop after sending an alert
        else:
            print("'lukket' still appears 10 times. Monitoring continues.")
    else:
        print("Could not check the page. Retrying...")

    # Wait for a random interval between 5 and 10 seconds
    delay = random.randint(5, 10)
    print(f"Waiting for {delay} seconds before the next check...")
    time.sleep(delay)
