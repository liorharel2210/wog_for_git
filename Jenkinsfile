pipeline {
    agent any
    tools{
        maven 'Dockertest'
    }
    stages{
        stage('Dockertest'){
            steps{
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/liorharel2210/wog_for_git']])
                sh 'docker clean install'
            }
        }
    }
}
