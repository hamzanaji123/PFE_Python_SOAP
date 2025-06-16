pipeline {
    agent any

    stages {
        stage('Préparation') {
            steps {
                echo 'Création de l’environnement virtuel...'
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip install --upgrade pip'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Tests') {
            steps {
                echo 'Exécution des tests...'
                bat 'venv\\Scripts\\pytest test_soap_client.py --junitxml=results.xml --html=report.html'
            }
        }
    }

    post {
        always {
            junit 'results.xml'
            archiveArtifacts artifacts: 'report.html', fingerprint: true
        }
    }
}

