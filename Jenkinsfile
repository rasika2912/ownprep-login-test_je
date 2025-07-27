
pipeline {
    agent any

    tools {
        python 'Python312'
    }

    environment {
        DISPLAY = ':0'
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo 'Cloned from GitHub or uploaded manually'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Test') {
            steps {
                sh 'python test_login_dropdown.py'
            }
        }
    }
}
