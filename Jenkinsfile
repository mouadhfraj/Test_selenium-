pipeline {
     agent { 
        node {
            label 'docker-agent-python'
            }
      }
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                    python -m pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    python -m add_product.py --alluredir=allure-results
                '''
            }
        }
        stage('Generate Allure Report') {
            steps {
                sh '''
                    allure generate allure-results --clean -o allure-report
                    allure open allure-report
                '''
            }
        }
    }
}
