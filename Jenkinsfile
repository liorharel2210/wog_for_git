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
        
        stage('Check Docker Compose') {
            steps {
                script {
                    def dockerComposeInstalled = sh(script: 'command -v docker-compose', returnStatus: true) == 0
                    if (!dockerComposeInstalled) {
                        echo 'Docker Compose is not installed. Installing Docker Compose...'
                        // Install Docker Compose without sudo
                        sh '''
                            curl -fsSL https://get.docker.com -o get-docker.sh
                            chmod +x get-docker.sh
                            ./get-docker.sh
                            rm get-docker.sh
                        '''
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
                sh 'docker build -t your_image_name:$BUILD_NUMBER .'
            }
        }
        
        stage('Run Docker Compose') {
            steps {
                sh 'docker-compose up'
            }
        }
        
        // Add more stages as needed
        
    }
}

def isMacOS() {
    return (env.PATH?.contains('/usr/bin') || env.PATH?.contains('/usr/sbin')) && env.PATH?.contains('/sbin') && env.PATH?.contains('/bin')
}
