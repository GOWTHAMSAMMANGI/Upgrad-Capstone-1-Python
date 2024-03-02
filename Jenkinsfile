pipeline {
    agent any
    environment {
        registry = "gowthamsammangi/upgrad-python1"
        registryCredential = 'dockerhub'
    }

    stages {
        stage('git checkout') {
            steps {
                git branch: 'project-1', url: 'https://github.com/GOWTHAMSAMMANGI/Upgrad-Capstone-1-Python.git'
            }
        }
        
        stage('Build docker image') {
            steps {
                script {
                  dockerImage = docker.build registry + ":v$BUILD_NUMBER"
              }
            }
        }
        stage('Upload Image'){
          steps{
            script {
              docker.withRegistry('', registryCredential) {
                dockerImage.push("v$BUILD_NUMBER")
                dockerImage.push('latest')
              }
            }
          }
        }
        stage('Remove Unused docker image') {
          steps{
            sh "docker rmi $registry:v$BUILD_NUMBER"
          }
        }
        stage('Deploying container to Kubernetes') {
           steps {
                sh "helm version"
                sh "echo helm installed succesfully"
                sh "helm install project-1 python-project --set appimage=${registry}:v${BUILD_NUMBER}"
            }
        }    
        stage('Monitoring tool prometheus container') {
           steps {
                sh "helm repo add prometheus-community https://prometheus-community.github.io/helm-charts"
                sh "helm repo update"
                sh "helm install my-kube-prometheus-stack prometheus-community/kube-prometheus-stack"
            }
        }
        

    }
}
