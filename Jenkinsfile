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

<<<<<<< HEAD
<<<<<<< HEAD
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


// pipeline {
//     agent any

//     stages {
//         stage('Checkout') {
//             steps {
//                 checkout([
//                     $class: 'GitSCM',
//                     branches: [[name: '*/main']],
//                     extensions: [],
//                     userRemoteConfigs: [[
//                         credentialsId: 'newtoken',
//                         url: 'https://github.com/rasika2912/ownprep-login-test_je.git'
//                     ]]
//                 ])
//             }
//         }

//         stage('Install Dependencies') {
//             steps {
//                 bat 'python --version'
//                 bat 'pip install --upgrade pip'
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


// pipeline {
//     agent any

//     tools {
//         python 'Python3'  // Make sure yeh Python Jenkins me configured hai
//     }

//     stages {
//         stage('Checkout') {
//             steps {
//                 checkout([
//                     $class: 'GitSCM',
//                     branches: [[name: '*/main']],
//                     userRemoteConfigs: [[
//                         credentialsId: 'newtoken',
//                         url: 'https://github.com/rasika2912/ownprep-login-test_je.git'
//                     ]]
//                 ])
//             }
//         }

//         stage('Install Dependencies') {
//             steps {
//                 bat 'python --version'
//                 bat 'pip install --upgrade pip'
//                 bat 'pip install -r requirements.txt'
//             }
//         }

//         stage('Run Selenium Tests') {
//             steps {
//                 bat 'pytest test_login.py test_login_dropdown.py --alluredir=allure-results --junitxml=results.xml --html=reports/reports.html --self-contained-html'
//             }
//         }

//         stage('Allure Report') {
//             steps {
//                 allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
//             }
//         }

//         stage('Publish HTML Report') {
//             steps {
//                 publishHTML target: [
//                     reportDir: 'reports',
//                     reportFiles: 'reports.html',
//                     reportName: 'Selenium Test Report',
//                     keepAll: true,
//                     alwaysLinkToLastBuild: true,
//                     allowMissing: false
//                 ]
//             }
//         }
//     }
// }

// pipeline {
//     agent any

//     tools {
//         python 'Python3'  // Ensure 'Python3' is set in Jenkins Global Tools
//     }

//     stages {
//         stage('Checkout') {
//             steps {
//                 checkout([
//                     $class: 'GitSCM',
//                     branches: [[name: '*/main']],
//                     userRemoteConfigs: [[
//                         credentialsId: 'newtoken',
//                         url: 'https://github.com/rasika2912/ownprep-login-test_je.git'
//                     ]]
//                 ])
//             }
//         }

//         stage('Install Dependencies') {
//             steps {
//                 bat 'python --version'
//                 bat 'pip install --upgrade pip'
//                 bat 'pip install -r requirements.txt'
//             }
//         }

//         stage('Run Selenium Tests') {
//             steps {
//                 bat 'pytest test_login_dropdown.py --alluredir=allure-results --junitxml=results.xml --html=reports/reports.html --self-contained-html'
//             }
//         }

//         stage('Allure Report') {
//             steps {
//                 allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
//             }
//         }

//         stage('Publish HTML Report') {
//             steps {
//                 publishHTML target: [
//                     reportDir: 'reports',
//                     reportFiles: 'reports.html',
//                     reportName: 'Selenium Test Report',
//                     keepAll: true,
//                     alwaysLinkToLastBuild: true,
//                     allowMissing: false
//                 ]
//             }
//         }
//     }

//     post {
//         always {
//             // Optional: Archive screenshots or logs
//             archiveArtifacts artifacts: '**/*.png', allowEmptyArchive: true
//         }
//     }
// }

pipeline {
    agent any

    environment {
        REPORT_DIR = "reports"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/rasika2912/ownprep-login-test_je.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run All Pytests') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    pytest test_login.py --html=reports/report.html --self-contained-html

                '''
            }
        }

        stage('Publish HTML Report') {
            steps {
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: 'Pytest HTML Report'
                ])
            }
        }
    }
}
