# AWS VM user data for kubernetes 
cd /opt
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl

sudo apt-get update && \
    sudo apt-get install docker.io -y
	
	
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/

# Cluster Setup
Assuming you have minikube or kubernetes cluster up and running with DNS and ingress controller working. 

sudo su
minikube start --vm-driver=none

# clone the repo

# docker registery setup
docker run -d   -p 5001:5000   --restart=always   --name registry   -v /var/registry:/var/lib/registry   registry:2

# start app
./start

# stop app
./stop

# Troubleshooting
kubectl logs deployment/flask-api
kubectl logs deployment/flask-reverse



