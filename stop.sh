#!/bin/bash

# Name and tag of the image
IMAGE_NAME="test_de_mon_model"

# Check if the image exists
if sudo docker images | grep -q "${IMAGE_NAME}"; then
    sudo docker-compose down
    sudo docker rm -f model_ml
    echo "Image ${IMAGE_NAME} exists. Removing..."
    sudo docker rmi "${IMAGE_NAME}"
else
    echo "Image ${IMAGE_NAME} does not exist."
fi

