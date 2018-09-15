pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        echo 'Running tests'
        sh 'python3 -m unittest test'
      }
    }
  }
}