pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        echo 'Running tests'
        sh 'python3 -m pytest --junitxml results.xml test.py'
      }
    }
  }
}