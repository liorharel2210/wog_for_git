pipeline {
    agent {
        docker {
            //
            image 'docker:latest'
            // 
            args '-v /Applications/Docker.app/'
        }
    }
    
    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker-hub-harelkop')
    }
    
    stages {
        stage('Check Docker') {
            steps {
                script {
                    def dockerInstalled = sh(script: 'command -v docker', returnStatus: true) == 0
                    if (!dockerInstalled) {
                        echo 'Docker is not installed. Installing Docker...'
                        // Install Docker without sudo
                        sh '''
                            curl -fsSL https://get.docker.com -o get-docker.sh
                            chmod +x get-docker.sh
                            ./get-docker.sh
                            rm get-docker.sh
                        '''
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
