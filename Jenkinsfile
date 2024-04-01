properties([[$class: 'ContainerSetDefinition', buildHostImage: <object of type it.dockins.dockerslaves.spec.ImageIdContainerDefinition>, sideContainers: []]])
pipeline {
    agent any
    environment {
    DOCKERHUB_CREDENTIALS = credentials('docker-hub-harelkop')
    }
    stages {
        stage('SCM Checkout') {
            steps{
                git branch: 'main', url: 'https://github.com/liorharel2210/wog_for_git.git'
                }
        }

        stage('Build Docker image') {
            steps {
                sh 'docker build -t harelkop/wog:$BUILD_NUMBER . '
            }
        }
        stage('login to dockerhub') {
            steps{
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('push image') {
            steps{
                sh 'docker push harelkop/wog:$BUILD_NUMBER'
            }
        }
    }
}
