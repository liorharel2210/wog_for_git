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
                script {
                    docker.build('myapp')
                }
            }
        }
        
        stage('Run') {
            steps {
                script {
                    docker.withRun('-d -p 8777:8777 -v $(pwd)/Scores.txt:/Scores.txt myapp') { c ->
                        // Run any additional setup commands if needed
                    }
                }
            }
        }
        
        // Add more stages as needed
        
        stage('Cleanup') {
            steps {
                script {
                    docker.image('myapp').stop()
                    docker.image('myapp').remove()
                }
            }
        }
    }
}

