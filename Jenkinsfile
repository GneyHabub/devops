pipeline {
  agent {
    docker {
      image 'python:3.9-slim'
      args '-u root'
    }

  }
  stages {
    stage('installation') {
      steps {
        sh 'python -m pip install --upgrade pip'
        sh 'pip install -r app_python/requirements.txt'
      }
    }

    stage('unit-tests') {
      steps {
        sh 'pytest'
      }
    }

  }
}