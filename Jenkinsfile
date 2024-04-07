pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the Git repository
                git branch: 'main', url: 'https://github.com/liorharel2210/wog_for_git.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                // Build Docker image using the Dockerfile in the repository
                script {
                    sh 'docker build -t wogfinal:1.0.6 .'
                }
            }
        }
        stage('Deploy Docker Container') {
            steps {
                // Deploy Docker containers using docker-compose.yml
                script {
                    sh 'docker-compose up -d'
                }
            }
        }
        stage('Test') {
            steps {
                // Run selenium tests using e2e.py
                script {
                    sh 'python e2e2.py'
                }
            }
        }
        stage('Finalize') {
            steps {
                // Terminate the container
                script {
                    sh 'docker-compose down'
                }
                // Push the new image to DockerHub
                script {
                    sh 'docker push <your_dockerhub_username>/wogfinal:1.0.6'
                }
            }
        }
    }
}
