properties([[$class: 'ContainerSetDefinition', buildHostImage: <object of type it.dockins.dockerslaves.spec.ImageIdContainerDefinition>, sideContainers: []], githubProjectProperty(displayName: 'wog', projectUrlStr: 'https://github.com/liorharel2210/wog_for_git.git/')]
pipeline {
    agent any

    // stages {
    //     stage('Checkout') {
    //         steps {
    //             checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[name: 'wog', url: 'https://github.com/liorharel2210/wog_for_git.git']])
    //         }
    //     }

    //     stage('Check Docker Version') {
    //         steps {
    //             sh 'docker --version'
        stage('Build Docker image') {
            steps {
                script {
                    dockerImage = docker.build('wogfinal:1.0.1'
                
                    
                
            }
        }
    }
}
