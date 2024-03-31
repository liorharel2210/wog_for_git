
pipeline {
    agent any
    
    stages {
        stage('Install Docker') {
            steps {
                // Install Docker
                script {
                    if (isUnix()) {
                        sh 'sudo -s apt-get update && sudo -s apt-get install -y docker.io'
                        sh 'sudo -s systemctl start docker'
                    } else {
                        echo 'Docker installation is only supported on Unix systems.'
                    }
                }
            }
        }
        
        stage('Install Docker Compose') {
            steps {
                // Install Docker Compose
                script {
                    if (isUnix()) {
                        sh 'sudo -s curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose'
                        sh 'sudo -s chmod +x /usr/local/bin/docker-compose'
                    } else {
                        echo 'Docker Compose installation is only supported on Unix systems.'
                    }
                }
            }
        }
        
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/liorharel2210/wog_for_git.git'
            }
        }
        
        stage('Build') {
            steps {
                sh 'docker build -t myapp .'
            }
        }
        
        stage('Run') {
            steps {
                sh 'docker run -d -p 8777:8777 -v $(pwd)/Scores.txt:/Scores.txt myapp'
            }
        }
        
        stage('Test') {
            steps {
                sh 'python e2e2.py'
            }
        }
        
        stage('Finalize') {
            steps {
                sh 'docker stop $(docker ps -q --filter ancestor=myapp)'
                sh 'docker tag myapp harelkopops/myapp:latest'
                sh 'docker push harelkopops/myapp:latest'
            }
        }
    }
}
