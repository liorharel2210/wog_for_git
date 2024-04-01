pipeline {
    agent any
    tools{
        maven 'maven'
    }
    stages{
        stage('Maven'){
            steps{
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/liorharel2210/wog_for_git']])
                sh 'mvn clean install'
            }
        }
    }
}
