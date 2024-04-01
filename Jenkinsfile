pipeline {
    agent any
    
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
                            sh get-docker.sh
                            rm get-docker.sh
                        '''
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
        
        stage('Build Docker image') {
            steps {
                sh "docker build -t harelkop/wog:\$BUILD_NUMBER ."
            }
        }
        
        stage('Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-harelkop', passwordVariable: 'DOCKERHUB_PASSWORD', usernameVariable: 'DOCKERHUB_USERNAME')]) {
                    sh "echo \$DOCKERHUB_PASSWORD | docker login -u \$DOCKERHUB_USERNAME --password-stdin"
                }
            }
        }
        
        stage('Push image') {
            steps {
                sh "docker push harelkop/wog:\$BUILD_NUMBER"
            }
        }
    }
}
