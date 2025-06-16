pipeline {
    agent any

    stages {
        stage('Préparation') {
            steps {
                echo 'Création de l’environnement virtuel...'
                bat 'cmd /c ""C:\\Users\\allo\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv venv"'
                bat 'cmd /c "venv\\Scripts\\pip install --upgrade pip"'
                bat 'cmd /c "venv\\Scripts\\pip install -r requirements.txt"'
            }
        }

        stage('Tests') {
            steps {
                echo 'Exécution des tests...'
                bat 'cmd /c "venv\\Scripts\\pytest test_soap_client.py --junitxml=results.xml --html=report.html"'
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
