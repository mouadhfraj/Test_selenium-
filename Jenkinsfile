pipeline {
    agent any // Exécuter sur n'importe quel nœud disponible.
    environment {
        ALLURE_RESULTS = 'allure-results' // Chemin vers les résultats Allure
        ALLURE_REPORT = 'allure-report'   // Chemin vers les rapports générés
    }
    stages {
       
        stage('Install Dependencies') {
            steps {
                // Installer un environnement virtuel Python et les dépendances
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Run Selenium Tests') {
            steps {
                // Exécuter les tests Selenium et générer les résultats Allure
                sh './venv/bin/pytest --alluredir=allure-results'
            }
        }
        stage('Generate Allure Report') {
            steps {
                // Générer les rapports Allure
                sh 'allure generate $ALLURE_RESULTS -o $ALLURE_REPORT --clean'
            }
        }
        stage('Publish Allure Report') {
            steps {
                // Publier les rapports Allure dans Jenkins
                allure([
                    results: [[path: "${env.ALLURE_RESULTS}"]],
                    reportBuildPolicy: 'ALWAYS'
                ])
            }
        }
    }
    post {
    failure {
        mail to: 'mouad.fraj@ensi-uma.tn',
             subject: "Build Failed: ${currentBuild.fullDisplayName}",
             body: "The build ${env.BUILD_URL} has failed."
    }
}

}
