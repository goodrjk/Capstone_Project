#!/usr/bin/env bash

# Step 1:
echo "Start docker service"
sudo systemctl start docker 
sudo docker version
#service docker.io status
#service docker.io start

# Step 1:
# Build image and add a descriptive tag
# The . is the path
echo "Build docker image"
docker build --tag=capstone .

# Step 2: 
# List docker images
docker image ls

# Step 3: 
# Run flask app
#docker run -p 8000:80 capstone

# Step 4:
# Create dockerpath
dockerpath=goodrjk/udacity_5:latest

# Step 5:  
# Authenticate & tag
echo "Docker ID and Image: $dockerpath"
docker tag capstone $dockerpath

# Step 6:
# Push image to a docker repository
echo "Push image to DockerHub"
docker login
docker push $dockerpath
#docker push goodrjk/udacity_4:tagname
