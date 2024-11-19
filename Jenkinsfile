pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
    environment {
        ALLURE_RESULTS = 'allure-results'  // Directory for Allure results
        ALLURE_REPORT = 'allure-report'    // Directory for Allure report
    }
    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Run the tests and generate Allure results
                    sh 'pytest --alluredir=allure-results'
                }
            }
        }
        stage('Generate Allure Report') {
            steps {
                script {
                    // Generate Allure report
                    sh "allure generate ${env.ALLURE_RESULTS} --clean -o ${env.ALLURE_REPORT}"
                }
            }
        }
        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: "${env.ALLURE_RESULTS}"]]
            }
        }
    }
    post {
        always {
            // Clean up the workspace
            deleteDir()
        }
    }
}
