# Variables
DOCKER_IMAGE=findbolig-nu
DOCKER_TAG=latest
CONTAINER_NAME=findbolig-nu
ENV_FILE=.env

# Build the Docker image
build:
	docker build -t $(DOCKER_IMAGE):$(DOCKER_TAG) .

# Run the Docker container
deploy:
	docker run --name $(CONTAINER_NAME) --env-file $(ENV_FILE) -d $(DOCKER_IMAGE):$(DOCKER_TAG)

# Stop and remove the container
stop:
	docker stop $(CONTAINER_NAME) || true && docker rm $(CONTAINER_NAME) || true
	docker system prune -f

# Logs
logs:
	docker logs -f $(CONTAINER_NAME)
