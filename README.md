# Flask API with two microservices hosted on kubernetes cluster  

>/reverse - { "message":"abcdefg" } → { "message":"gfedcba" }    
>/api - { "message":"abcdefg" } → { "message":"gfedcba", "rand": 0.12345678 }    
   
>/api endpoint delegates the message reversal task to /reverse    

## DEV setup  

### Cluster Setup
Assuming you have minikube or kubernetes cluster up and running with DNS and ingress controller working.   
  
`sudo su`  
`minikube start --vm-driver=none`  
`minikube addons enable ingress`  
`minikube addons enable kube-dns`  
  
### clone the repo  
`git clone https://github.com/nitesh8860/flask-minikube.git`  
  
### docker registery setup  
`docker run -d   -p 5001:5000   --restart=always   --name registry   -v /var/registry:/var/lib/registry   registry:2`  
  
### start app  
`./start`  
  
### stop app  
`./stop`  
  
### Internal testing  
`kubectl get svc | grep flask-api`  
pick up the CLUSTER-IP  
`curl -XPOST http://<CLUSTER-IP>:5000/api -d '{    "message": "abcdef"  }' -H "Content-Type: application/json"`  
  
### Troubleshooting  
`kubectl logs deployment/flask-api`  
`kubectl logs deployment/flask-reverse`  

## Gcloud setup
### Build and Push your image on gcloud  
`gcloud builds --project projectName submit --tag gcr.io/projectName/flask-reverse:v1 ./reverse/`  
`gcloud builds --project projectName submit --tag gcr.io/projectName/flask-api:v1 ./api/`  
Create a cluster on gcloud.  
`kubectl apply -f deploy-gcloud-reverse.yaml`  
`kubectl apply -f deploy-gcloud-api.yaml`  
Get service URLs   
`kubectl get services --namespace=flask`  
Apply Ingress post changing the hostname in ingress.yml
`kubectl apply -f ingress.yml`  

I will be creating my own system diagram soon, till then, a more or less similar and nice diagram from gcloud   
![alt text](https://cloud.google.com/solutions/images/creating-cicd-pipeline-with-kubernetes-engine-architecture.svg "System Diagram")   
    
    
## Continuous delivery pipeline with jenkins and Gcloud
![alt text](https://cloud.google.com/solutions/images/jenkins-cd-container-engine.svg "CICD pipeline with jenkins and gcloud")   

here in this diagram, Backend is /reverse and Frontend is /api services.

* Avoid Downtimes with the help of Canary deployments.
* Create seperate namespaces to deploy in development, testing and production environments.
> [Source : Google](https://cloud.google.com/solutions/continuous-delivery-jenkins-kubernetes-engine)

