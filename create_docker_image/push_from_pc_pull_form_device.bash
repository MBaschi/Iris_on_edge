#!/bin/bash

# Define variables
IMAGE_NAME=$1
DOCKER_USERNAME="your-docker-username"
DEVICE_USERNAME="your-device-username"
DEVICE_IP="your-device-ip"

# Push the image to the registry
docker tag $IMAGE_NAME $DOCKER_USERNAME/$IMAGE_NAME
docker push $DOCKER_USERNAME/$IMAGE_NAME

# Connect to the device and pull the image
ssh $DEVICE_USERNAME@$DEVICE_IP << EOF
  until docker pull $DOCKER_USERNAME/$IMAGE_NAME; do
    echo "Waiting for image to be available..."
    sleep 5
  done
EOF