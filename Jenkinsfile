pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                // Checkout your source code from GitHub
                git branch: 'main', url: 'https://github.com/liorharel2210/wog_for_git.git'
                
                // Build Docker image using Dockerfile
                script {
                    docker.build("python:3.9")
                }
            }
        }
    }
}
