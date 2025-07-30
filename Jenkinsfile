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

=======
>>>>>>> 5630782 (Added working Jenkinsfile)

=======
>>>>>>> 4694ee3 (Fix Jenkinsfile checkout syntax)
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

pipeline {
    agent any

    tools {
        python 'Python3'  // Jenkins me defined Python tool ka naam (manage Jenkins > Global Tool Configurations)
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
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
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat 'pytest test_login.py test_login_dropdown.py --alluredir=allure-results --junitxml=results.xml --html=reports.html'
            }
        }

        stage('Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }

        stage('Publish HTML Report') {
            steps {
                publishHTML target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'reports.html',
                    reportName: 'Test Execution Report'
                ]
            }
        }
    }
}














