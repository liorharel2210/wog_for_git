
pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/liorharel2210/wog_for_git.git'
            }
        }
        
        stage('Build') {
            steps {
                sh 'docker version'
                   'docker info'
                   'docker build -t myapp .'
            }
        }
        
        stage('Run') {
            steps {
                sh 'docker-compose up'
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
