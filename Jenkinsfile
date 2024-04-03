pipeline {
    agent any
    
    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker-hub-harelkop')
    }
    
    stages {
        stage('Check Docker') {
            when {
                // Skip Docker installation if running on macOS
                expression { !isMacOS() }
            }
            steps {
                script {
                    def dockerInstalled = sh(script: 'command -v docker', returnStatus: true) == 0
                    if (!dockerInstalled) {
                        echo 'Docker is not installed. Please install Docker manually.'
                        currentBuild.result = 'ABORTED'
                        return
                    } else {
                        echo 'Docker is already installed.'
                    }
                }
            }
        }
        
        stage('SCM Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/liorharel2210/wog_for_git.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Change directory to where Dockerfile is located
                    dir('/Users/liorharel/wog_for_git') {
                        // Build Docker image using Dockerfile
                        sh 'docker build -t wogfinalapp:1.1.4 .'
                    }
                }
            }
        }
        
        // Add more stages as needed
        
    }
}

def isMacOS() {
    return (env.PATH?.contains('/usr/bin') || env.PATH?.contains('/usr/sbin')) && env.PATH?.contains('/sbin') && env.PATH?.contains('/bin')
}
