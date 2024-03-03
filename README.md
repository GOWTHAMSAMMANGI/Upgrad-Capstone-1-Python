# Deploying a Python Web Application on Kubernetes Cluster

This deployment will focus on containerization using `Docker`, `Kubernetes` orchestration, the implementation of a `CI/CD` pipeline, and setting up effective monitoring and logging solutions. The goal is to automate deployment processes, enhance scalability, and leverage modern technologies for efficient web application management.

## Prerequisites

This tools should be installed :
- Docker
- Kubectl
- Terraform
- AWS EKS
- Helm
- Jenkins

## Step 1: Create Python Flask Web Application

Create a file and name it `app.py`. You file will look like this:
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

## Step 2: Containerize Python Flask Web Application

- Create a file and name it `requirements.txt` and put the name name of the dependencies. In our case the only dependency we need is `flask`. 
- Write the Dockerfile for the application. Your Dockerfile will look like this:
 
```
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 3000
COPY . .
CMD ["flask", "run"]
```
In this project we are running the application on port 3000 but you can choose any port number.

- Build image from Dockerfile and tag it with your dockerhub repository name. e.g.
`Docker build -t iamsauravsingh/python-app` and push it to dockerhub.

## Step 3: Set Up AWS EKS Cluster

- Create a AWS EKS cluster using Terraform.

## Step 4: Create a helm chart

- To Create a sample helm chart use command

```
helm create python-project
```

- Now we have to write `deployment.yaml` and `service.yaml` files and copy them to python-project/template/ directory

## Step 5: Implement Jenkins CI/CD Pipeline

- Log in to Jenkins server and install some plugins such as:  
a) Docker Pipeline  
b) Pipeline Utilities

- Now click `manage jenkins` and then go to `credentials` and create a new credentials for your dockerhub login. 

- Now run the pipeline using GIT SCM and specify the jenkins file

- Now click on `Build Now` and after sometime you will get similar results like this: 
![image](https://github.com/GOWTHAMSAMMANGI/Upgrad-Capstone-1-Python/assets/62459668/9b71fadc-50eb-4b1a-bae4-243358d30647)


## Step 6:Testing and Verification

Here we will verify that our application is successfully deployed on kubernetes or not.
- Now go to the kubernetes cluster and run `kubectl get pods` you will get something like this:

![image](https://github.com/GOWTHAMSAMMANGI/Upgrad-Capstone-1-Python/assets/62459668/95d1e17e-177e-48b3-93e5-4674e4600683)

## Step 7: Monitoring and Logging

In this Project we are using Prometheus and grafana to monitor our application. We are using helm charts to setup prometheus and Grafana. To setup prometheus and Grafana use one more stage in pipeline with below commands:
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts  
helm repo update
helm install my-kube-prometheus-stack prometheus-community/kube-prometheus-stack
```

Now to go the kubernetes cluster and change the service type to NodePort service named `my-kube-prometheus-stack-grafana` run the command `kubectl get svc` you will get similar output: 
![image](https://github.com/GOWTHAMSAMMANGI/Upgrad-Capstone-1-Python/assets/62459668/95330f50-eaca-469e-8538-7b1540741e89)

Now run the command `kubectl get svc my-kube-prometheus-stack-grafana` and you will be redirected to grafana dashboard. For username and password go to kubernetes cluster and run the command `kubectl edit secret my-kube-prometheus-stack-grafana`. You will get similar results like this: 
```

# Please edit the object below. Lines beginning with a '#' will be ignored,
# and an empty file will abort the edit. If an error occurs while saving this file will be
# reopened with the relevant failures.
#
apiVersion: v1
data:
  admin-password: cHJvbS1vcGVyYXRvcg==
  admin-user: YWRtaW4=
  ldap-toml: ""
kind: Secret
metadata:
  annotations:
    meta.helm.sh/release-name: my-kube-prometheus-stack
    meta.helm.sh/release-namespace: default
  creationTimestamp: "2023-10-03T16:44:48Z"
  labels:
    app.kubernetes.io/instance: my-kube-prometheus-stack
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/name: grafana
    app.kubernetes.io/version: 10.1.2
    helm.sh/chart: grafana-6.59.5
  name: my-kube-prometheus-stack-grafana
  namespace: default
  resourceVersion: "151556"
  uid: 5a9f95bd-a28b-4754-801e-69f67a09a5bf
type: Opaque
```
To decode this password use command:
```bash
echo -n "YWRtaW4==" | base64 --decode
echo -n "cHJvbS1vcGVyYXRvcg==" | base64 --decode
```
Now login to Grafana and create a new dashboard. And you will get a similar output
![image](https://github.com/GOWTHAMSAMMANGI/Upgrad-Capstone-1-Python/assets/62459668/386b0d8e-ca55-4ca8-8e0a-2b94244ed3dc)


### Thank you.
