#!/usr/bin/env bash

# Step 1:
# Build image and add a descriptive tag
# The . is the path
docker build --tag=gjohn_ .

# Step 2: 
# List docker images
docker image ls

# Step 3: 
# Run flask app
docker run -p 8000:80 gjohn_local

# Step 4:
# Create dockerpath
dockerpath=goodrjk/udacity_4:firstimage

# Step 5:  
# Authenticate & tag
echo "Docker ID and Image: $dockerpath"
docker tag dd441368f48a $dockerpath

# Step 6:
# Push image to a docker repository
docker login
docker push $dockerpath
#docker push goodrjk/udacity_4:tagname
