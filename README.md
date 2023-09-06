# Flask API with Two Microservices on Kubernetes Cluster

This project demonstrates a Flask API with two microservices deployed on a Kubernetes cluster. The microservices include:

1. `/reverse`: Reverses a given message.
2. `/api`: Accepts a message and delegates the reversal task to `/reverse` while also adding a random number.

## Development Setup

### Cluster Setup

Ensure you have Minikube or a Kubernetes cluster running with DNS and an Ingress controller.

```shell
sudo su
minikube start --vm-driver=none
minikube addons enable ingress
minikube addons enable kube-dns
```

### Clone the Repo

```shell
git clone https://github.com/nitesh8860/flask-minikube.git
```

### Docker Registry Setup

```shell
docker run -d -p 5001:5000 --restart=always --name registry -v /var/registry:/var/lib/registry registry:2
```

### Start App

```shell
./start
```

### Stop App

```shell
./stop
```

### Internal Testing

Get the Cluster IP of the `/api` service:

```shell
kubectl get svc | grep flask-api
```

Use `curl` to test the API:

```shell
curl -XPOST http://<CLUSTER-IP>:5000/api -d '{"message": "abcdef"}' -H "Content-Type: application/json"
```

### Troubleshooting

Check the logs of the deployments:

```shell
kubectl logs deployment/flask-api
kubectl logs deployment/flask-reverse
```

## Google Cloud Setup

### Build and Push Images to GCR

```shell
gcloud builds --project projectName submit --tag gcr.io/projectName/flask-reverse:v1 ./reverse/
gcloud builds --project projectName submit --tag gcr.io/projectName/flask-api:v1 ./api/
```

### Create a Kubernetes Cluster on Google Cloud

Deploy the services:

```shell
kubectl apply -f deploy-gcloud-reverse.yaml
kubectl apply -f deploy-gcloud-api.yaml
```

Get service URLs:

```shell
kubectl get services --namespace=flask
```

Apply Ingress after changing the hostname in `ingress.yml`:

```shell
kubectl apply -f ingress.yml
```

### Google Cloud Architecture

![Google Cloud Architecture Diagram](https://cloud.google.com/static/architecture/images/creating-cicd-pipeline-with-kubernetes-engine-architecture.svg)

## Continuous Delivery Pipeline with Jenkins and Google Cloud

![CICD Pipeline with Jenkins and Google Cloud](https://cloud.google.com/static/architecture/images/jenkins-cd-container-engine.svg)

In this pipeline, the `/reverse` service is the backend, and the `/api` service is the frontend.

- Avoid downtimes using Canary deployments.
- Create separate namespaces for development, testing, and production environments.

[Source: Google](https://cloud.google.com/solutions/continuous-delivery-jenkins-kubernetes-engine)

Enjoy exploring this Flask API with microservices on a Kubernetes cluster!
