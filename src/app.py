import requests
from bs4 import BeautifulSoup
import time
import random

# URL to monitor
URL = "https://www.findbolig.nu/da-dk/udlejere"

# User-Agent header to mimic a browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

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

# Function to send an alert (replace this with your notification logic)
def send_alert():
    print("ALERT: 'lukket' no longer appears 10 times on the page! Check the website immediately!")

# Monitor the page in a loop
while True:
    status = check_if_lukket_appears()
    if status is not None:
        if not status:  # If "lukket" does not appear exactly 10 times
            send_alert()
            break  # Exit the loop after sending an alert
        else:
            print("'lukket' still appears 10 times. Monitoring continues.")
    else:
        print("Could not check the page. Retrying...")

    delay = random.randint(5, 10)
    print(f"Waiting for {delay} seconds before the next check...")
    time.sleep(delay)