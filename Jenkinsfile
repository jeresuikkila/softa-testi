pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        echo 'Running tests'
        sh 'python -m pytest --junitxml results.xml test.py'
      }
    }
  }
}