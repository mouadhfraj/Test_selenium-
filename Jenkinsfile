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
        stage('Setup Environment') {
            steps {
                sh '''
                    
                     if command -v apt >/dev/null; then
                        apt update && apt install -y google-chrome-stable
                    elif command -v apk >/dev/null; then
                        apk update && apk add chromium
                    else
                        echo "Package manager not found!" >&2
                        exit 1
                    fi
                '''
            }}
        stage('Install Dependencies') {
            steps {
                sh '''
                    export PATH=$PATH:/home/jenkins/.local/bin
                    python3 -m pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    export PATH=$PATH:/home/jenkins/.local/bin
                    python3 -m pytest add_product.py --alluredir=allure-results
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
