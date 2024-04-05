pipeline {
    agent any
    
    
        
        stage('SCM Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[name: 'wog', url: 'https://github.com/liorharel2210/wog_for_git.git']])
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    
                    
                        // Build Docker image using Dockerfile
                        sh 'docker build -t wogfinalapp:1.1.4 .'
                    }
                }
            }
        }
        
        // Add more stages as needed
        
    }
}
