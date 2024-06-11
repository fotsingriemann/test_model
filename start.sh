#!/bin/bash

# Name and tag of the image
IMAGE_NAME="test_de_mon_model"
CONTAINER_NAME="model_ml"

# Check if the image exists
if sudo docker images | grep -q "${IMAGE_NAME}"; then
    echo "Impossible to start because the Image ${IMAGE_NAME} exists."
else
    sudo docker build -t ${IMAGE_NAME} .
    docker-compose up
fi

