
// pipeline {
//     agent any

//     tools {
//         python 'Python312'
//     }

//     environment {
//         DISPLAY = ':0'
//     }

//     stages {
//         stage('Clone Repo') {
//             steps {
//                 echo 'Cloned from GitHub or uploaded manually'
//             }
//         }

//         stage('Install Dependencies') {
//             steps {
//                 sh 'pip install -r requirements.txt'
//             }
//         }

//         stage('Run Test') {
//             steps {
//                 sh 'python test_login_dropdown.py'
//             }
//         }
//     }
// }
pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'python --version'
                bat 'pip install --upgrade pip'
                bat 'pip install pytest pytest-html allure-pytest'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat 'pytest tests --alluredir=report --junitxml=result.xml --html=reports.html'
            }
        }

        stage('Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'report']]
            }
        }

        stage('Publish HTML Report') {
            steps {
                publishHTML target: [
                    reportDir: '.',
                    reportFiles: 'reports.html',
                    reportName: 'Selenium Test Report'
                ]
            }
        }
    }
}
