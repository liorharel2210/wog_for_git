pipeline {
    agent any

    environment {
        dockerImage = ''
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/liorharel2210/wog_for_git.git']])
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    dockerImage = docker.build('wogfinal')
                }
            }
        }
    }
}
