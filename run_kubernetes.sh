#!/usr/bin/env bash
# Step 1:
# This is your Docker ID/path
dockerpath=goodrjk/udacity_4:firstimage
# Step 2
# Run the Docker Hub container with kubernetes
kubectl create deployment kb4 --image=goodrjk/udacity_4:firstimage --port=80
# Step 3:
# List kubernetes pods
kubectl get pods --all-namespaces
# Step 4:
# Forward the container port to a host
#kubectl expose deployment udacity4 --type="NodePort" --port=80
kubectl expose deployment kb4 --type=LoadBalancer --name=kb4-service --port=80 --target-port=80
sleep 180
kubectl port-forward deployment/kb4 8000:80
kubectl logs --selector app=kb4

