# Variables
DOCKER_IMAGE=findbolig-nu
DOCKER_TAG=latest
PYTHON_FILE=src/app.py
ENV_FILE=.env
CONTAINER_NAME=findbolig-nu

# Build the Docker image
build:
	docker build -t $(DOCKER_IMAGE):$(DOCKER_TAG) .

# Run the Docker container with the .env file
run:
	docker run --env-file $(ENV_FILE) $(DOCKER_IMAGE):$(DOCKER_TAG)

deploy:
	docker run --name $(CONTAINER_NAME) --env-file $(ENV_FILE) -d $(DOCKER_IMAGE):$(DOCKER_TAG)

# Run the Docker container in test mode
test:
	docker run --env-file $(ENV_FILE) -e TEST_MODE=True $(DOCKER_IMAGE):$(DOCKER_TAG)

# Install Python dependencies with Poetry
install:
	poetry install

# Run the application locally
run-local:
	poetry run python $(PYTHON_FILE)

# Clean up unused Docker images and containers
clean:
	docker system prune -f

# Help message
help:
	@echo "Usage:"
	@echo "  make build       - Build the Docker image"
	@echo "  make run         - Run the Docker container"
	@echo "  make test        - Run the Docker container in test mode"
	@echo "  make install     - Install Python dependencies with Poetry"
	@echo "  make run-local   - Run the application locally with Poetry"
	@echo "  make clean       - Clean up unused Docker resources"
