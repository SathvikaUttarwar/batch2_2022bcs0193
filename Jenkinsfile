pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "yourdockerhubusername/batch2_2022bcs0193"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/yourusername/batch2_2022bcs0193.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Model Training') {
            steps {
                sh 'python train.py'
            }
        }

        stage('Model Evaluation') {
            steps {
                sh 'python evaluate.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-pass', variable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u yourdockerhubusername --password-stdin'
                }
                sh 'docker push $DOCKER_IMAGE'
            }
        }
    }
}
