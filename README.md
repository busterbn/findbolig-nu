# findbolig-nu

This application notifies you when external waiting lists open up on [findbolig.nu](https://www.findbolig.nu/).

## How to Deploy the Script

1. **Set Up a Pushover Account:**
   - Create a [Pushover account](https://pushover.net/) and get your credentials:
     - **User Key**
     - **API Token**
   - Download the Pushover app to your iPhone from the [App Store](https://apps.apple.com/app/pushover-notifications/id506088175).

2. **Set Up the Environment:**
   Export the necessary environment variables to keep your credentials secure. Run the following commands in your terminal:

   ```bash
   export PUSHOVER_USER_KEY=your_user_key_here      # Replace with your Pushover User Key
   export PUSHOVER_API_TOKEN=your_api_token_here    # Replace with your Pushover API Token
   ```

3. **Install Poetry:**
   Ensure you have Poetry installed. If not, install it using the following command:

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

   Confirm the installation:

   ```bash
   poetry --version
   ```

4. **Set Up the Project:**
   Navigate to the project directory and install the dependencies using Poetry:

   ```bash
   poetry install
   ```

   Activate the virtual environment:

   ```bash
   poetry shell
   ```

5. **Run the Script:**
   Execute the script within the Poetry-managed environment:

   ```bash
   python script_name.py
   ```

6. **Receive Notifications:**
   When the waiting lists open, you will receive a Pushover notification with an alarm sound on your iPhone.

## Notes
- Replace placeholder values (e.g., `your_user_key_here`, `your_api_token_here`) with your actual Pushover credentials.
- Ensure that your `.env` file is kept secure and is listed in `.gitignore` to prevent sensitive information from being committed.
