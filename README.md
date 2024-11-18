# findbolig-nu

This application notifies you when the external waiting lists open up on [findbolig.nu](https://www.findbolig.nu/).

## How to use

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/busterbn/findbolig-nu.git
   cd findbolig-nu
   ```

2. **Sign Up for Pushover:**
   - Create a [Pushover account](https://pushover.net/).
   - Generate a **User Key** and **API Token** by creating a service in Pushover.

3. **Set Up Environment Variables:**
   - Export the necessary environment variables to keep your credentials secure. Run the following commands in your terminal:
     ```bash
     export PUSHOVER_USER_KEY=your_user_key_here      # Replace with your Pushover User Key
     export PUSHOVER_API_TOKEN=your_api_token_here    # Replace with your Pushover API Token
     ```

4. **Choose a Deployment Option**:
   - Proceed with either **Local Deployment** or **Docker Deployment** as described below.

---

## Deployment Options

### 1. Local Deployment

#### Step 1: Install Poetry
```bash
pip install poetry
```

#### Step 2: Install the dependencies
```bash
poetry install
```

#### Step 3: Start the application
```bash
poetry run src/app.py
```

#### Or if you're a pro, use make
```bash
make init  # Installs dependencies
make run   # Starts the application
```

---

### 2. Docker Deployment (Recommended)

#### Step 1: Create a `.env` File
Create a `.env` file in the project root and add your Pushover credentials:
```env
PUSHOVER_USER_KEY=your_user_key_here
PUSHOVER_API_TOKEN=your_api_token_here
TEST_MODE=False  # Set to True for testing
```

#### Step 2: Build the Docker Image
```bash
make build
```

#### Step 3: Run the Docker Container
```bash
make run
```

#### Step 4: The application is now running


For test mode, override the `TEST_MODE` environment variable:
```bash
make test
```

---
