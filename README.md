# findbolig-nu

This application notifies you when external waiting lists open up on [findbolig.nu](https://www.findbolig.nu/).

## How to Deploy the Script

1. **Sign up for Twilio:**
   - Create a [Twilio account](https://www.twilio.com/) and get your Twilio credentials:
     - **Account SID**
     - **Auth Token**
   - Purchase a Twilio phone number to make calls or send SMS.

2. **Set Up the Environment:**
   Export the necessary environment variables to keep your credentials secure. Run the following commands in your terminal:

   ```bash
   export TWILIO_AUTH_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXX      # Replace with your Twilio Auth Token
   export ACCOUNT_SID=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX      # Replace with your Twilio Account SID
   export TWILIO_PHONE_NUMBER="+1234567890"                 # Replace with your Twilio phone number
   export YOUR_PHONE_NUMBER="+1987654321"                   # Replace with your personal phone number

3. **Install Poetry: Ensure you have Poetry installed. If not, install it using the following command:**

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -

4. **Confirm the installation:**

    ```bash
    poetry --version

4. **Set Up the Project: Navigate to the project directory and install the dependencies using Poetry:**

    ```bash
    poetry install
    
5. **Activate the virtual environment:**

    ```bash
    poetry shell
6. **Run the Script: Execute the script within the Poetry-managed environment:**

    ```bash
    python script_name.py

7. **Receive Notifications: The script will call your phone number when the waiting lists open.**