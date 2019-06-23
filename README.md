AWS VM user data
###

cd /opt
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl

sudo apt-get update && \
    sudo apt-get install docker.io -y
	
	
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/

###
Start minikube in VM
###

sudo su
minikube start --vm-driver=none


###
setup docker registery, app, deployment, service and ingress
###
docker run -d   -p 5001:5000   --restart=always   --name registry   -v /var/registry:/var/lib/registry   registry:2

docker build -t localhost:5001/flask:latest .
docker push localhost:5001/flask:latest

kubectl apply -f deployment.yml
kubectl apply -f service.yml
kubectl apply -f ingress.yml

kubectl logs deployment/flask



