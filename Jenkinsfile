pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the Git repository
                git branch: 'main', url: 'https://github.com/liorharel2210/wog_for_git.git
            }
        }
        stage('Build Docker Image') {
            steps {
                // Build Docker image using the Dockerfile in the repository
                script {
                    docker.build('wogfinal', '-f Dockerfile .')
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
    }
}
