# Base image with Python
FROM python:3.13-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install Poetry using pip
RUN apt-get update && apt-get install -y curl build-essential \
    && pip install poetry \
    && apt-get clean

# Copy the project files to the container
COPY . /app

# Install dependencies using Poetry
RUN poetry install --no-dev

# Run the application
CMD ["poetry", "run", "python", "src/app.py"]
