// pipeline {
//     agent any

//     stages {
//         stage('Install Dependencies') {
//             steps {
//                 bat 'python --version'
//                 bat 'pip install --upgrade pip'
//                 bat 'pip install pytest pytest-html allure-pytest'
//             }
//         }

//         stage('Run Selenium Tests') {
//             steps {
//                 // Optional: Show files for debugging
//                 bat 'dir'

//                 // ✅ Corrected file name
//                 bat 'pytest test_login_dropdown.py --alluredir=report --junitxml=result.xml --html=reports.html'
//             }
//         }

//         stage('Allure Report') {
//             steps {
//                 allure includeProperties: false, jdk: '', results: [[path: 'report']]
//             }
//         }

//         stage('Publish HTML Report') {
//             steps {
//                 publishHTML target: [
//                     reportDir: '.',
//                     reportFiles: 'reports.html',
//                     reportName: 'Selenium Test Report'
//                 ]
//             }
//         }
//     }
// }

// pipeline {
//     agent any

//     stages {
//         stage('Install Dependencies') {
//             steps {
//                 bat 'python --version'
//                 bat 'pip install --upgrade pip'

//                 // Added webdriver-manager
//                 bat 'pip install pytest pytest-html allure-pytest webdriver-manager'
//             }
//         }

//         stage('Run Selenium Tests') {
//             steps {
//                 bat 'dir'
//                 bat 'pytest test_login_dropdown.py --alluredir=report --junitxml=result.xml --html=reports.html'
//             }
//         }

//         stage('Allure Report') {
//             steps {
//                 allure includeProperties: false, jdk: '', results: [[path: 'report']]
//             }
//         }

//         stage('Publish HTML Report') {
//             steps {
//                 publishHTML target: [
//                     reportDir: '.',
//                     reportFiles: 'reports.html',
//                     reportName: 'Selenium Test Report'
//                 ]
//             }
//         }
//     }
// }


pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    extensions: [],
                    userRemoteConfigs: [[
                        credentialsId: 'newtoken',
                        url: 'https://github.com/rasika2912/ownprep-login-test_je.git'
                    ]]
                ])
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python --version'
                bat 'pip install --upgrade pip'
                bat 'pip install pytest pytest-html allure-pytest webdriver-manager'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat 'dir'
                bat 'pytest test_login_dropdown.py --alluredir=report --junitxml=result.xml --html=reports.html'
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



















