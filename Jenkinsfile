pipeline {
    agent any

    stages {
        stage('Préparation') {
            steps {
                echo 'Installation des dépendances...'
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Tests') {
            steps {
                echo 'Exécution des tests...'
                sh './venv/bin/pytest test_soap_client.py --junitxml=results.xml --html=report.html'
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
