# Cluster Setup
Assuming you have minikube or kubernetes cluster up and running with DNS and ingress controller working. 

sudo su
minikube start --vm-driver=none
minikube addons enable ingress
minikube addons enable kube-dns

# clone the repo
git clone https://github.com/nitesh8860/flask-minikube.git

# docker registery setup
docker run -d   -p 5001:5000   --restart=always   --name registry   -v /var/registry:/var/lib/registry   registry:2

# start app
./start

# stop app
./stop

# Troubleshooting
kubectl logs deployment/flask-api
kubectl logs deployment/flask-reverse



