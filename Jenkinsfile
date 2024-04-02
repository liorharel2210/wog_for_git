pipeline {
    agent {
        docker {
            //
            image 'docker:latest'
            // 
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    
    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker-hub-harelkop')
    }
    
    stages {
        stage('Check Docker Compose') {
            steps {
                script {
                    def dockerComposeInstalled = sh(script: 'command -v docker-compose', returnStatus: true) == 0
                    if (!dockerComposeInstalled) {
                        echo 'Docker Compose is not installed. Please install Docker Compose manually.'
                        currentBuild.result = 'ABORTED'
                        return
                    } else {
                        echo 'Docker Compose is already installed.'
                    }
                }
            }
        }
        
        stage('SCM Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/liorharel2210/wog_for_git.git'
            }
        }
        
        stage('Build Docker image') {
            steps {
                sh 'docker build -t wogfinal:$BUILD_NUMBER .'
            }
        }
        
        stage('Run Docker Compose') {
            steps {
                sh 'docker-compose up'
            }
        }
        
        //
        
    }
}
