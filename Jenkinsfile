pipeline {
  agent any
  stages {
    stage('Install requirements') {
      steps {
        echo 'Installing requirements'
        sh 'pip3 install -U -r requirements.txt'
      }
    }

    stage('Test') {
      steps {
        echo 'Running tests'
        sh 'python3 -m pytest --junitxml results.xml test.py'
      }
    }

    post {
        always {
            junit 'results.xml'
        }
    }
  }
}