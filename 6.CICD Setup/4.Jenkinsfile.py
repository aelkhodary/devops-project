"""
https://www.jenkins.io/
# Documentation -> Jenkins Pipeline
https://www.jenkins.io/doc/book/pipeline/
Two type of jenkins files 
Declarative versus Scripted Pipeline syntax
# Declarative is the easer one .
"""
pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'echo building' 
            }
        }
        stage('Test') { 
            steps {
                echo 'testing' 
            }
        }
        stage('Deploy') { 
            steps {
                sh 'echo deploying' 
            }
        }
    }
}

