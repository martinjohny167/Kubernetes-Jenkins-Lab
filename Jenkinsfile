pipeline {
    agent {
        docker {
            image 'python:3.9'
            args '-u root'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pip install pytest pytest-cov pyinstaller'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m pytest --cov=. --junitxml=test-reports/test-results.xml'
            }
            post {
                always {
                    junit 'test-reports/test-results.xml'
                }
            }
        }
        stage('Deliver') {
            steps {
                sh 'pyinstaller -F app.py'
                archiveArtifacts artifacts: 'dist/app', fingerprint: true
            }
        }
    }
} 