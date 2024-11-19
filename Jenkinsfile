pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
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
                    sh 'python3 add_product.py'
                    sh 'python3 update_product.py'
                    sh 'python3 delete_product.py'
                }
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
