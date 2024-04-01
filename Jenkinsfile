pipeline {
    agent any
    tools{
        docker 'Dockertest'
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
