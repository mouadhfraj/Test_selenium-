pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
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
