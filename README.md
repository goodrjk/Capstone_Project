# Capstone_Project
## Capstone Project for Udacity Cloud Devops Engineer

## CircleCI Pipeline Jobs

### lint-code
	Check Dockerfile with hadolint  
	Check app.py with pylint
### docker-load
	Build the docker image for app.py
	Push the newly created docker image to DockerHub
### deploy-infrastructure
	Create the EC2 for the Kubernetes cluster using cloudformation
	Name the stack using the contents of the name.txt file concatenating it with Capstone-.
	If name.txt contains BLUE, stack name will be Capstone-BLUE
	Save the IP address of EC2 server
### configure-infrastructure
	Using Ansible load kubectl, minikube and docker
	Using Ansible start minikube
### deploy-docker
	Using Ansible deploy created docker image from DockerHub to Kubernetes cluster
### cleanup
	Delete all old Capstone AWS stacks
