pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[name: 'wog', url: 'https://github.com/liorharel2210/wog_for_git.git']])
            }
        }

        stage('Check Docker Version') {
            steps {
                sh 'docker --version'
        
                
                    
                
            }
        }
    }
}
