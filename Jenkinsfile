pipeline {
    agent {
    docker {
        image 'python:3'
        args '-v /var/run/docker.sock:/var/run/docker.sock'
    }
}

    environment {
        PYTHON = '/usr/local/bin/python'  // Path to Python in the container
    }

    stages {
        
        stage('Install Dependencies') {
            steps {
                sh '''
                    ${PYTHON} -m pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    ${PYTHON} -m add_product.py --alluredir=allure-results
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
