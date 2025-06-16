pipeline {
    agent any

    stages {
        stage('Exécution des tests') {
            steps {
                echo 'Lancement du script .bat...'
                bat 'run_tests.bat'
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
