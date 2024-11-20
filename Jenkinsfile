pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'docker pull python:3'
                sh 'docker run python:3 --version'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'docker run python:3 python -m pip install -r requirements.txt'
                sh 'docker run python:3 python -m add_product.py --alluredir=allure-results'
            }
        }
    }
}
