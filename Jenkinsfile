pipeline {
  agent {
    docker {
      image 'python:3-slim'
    }

  }
  stages {
    stage('deps') {
      steps {
        sh '''
                    python -m pip install --upgrade pip
                    pip install -r app_python/requirements.txt
                '''
      }
    }

    stage('unit-tests') {
      steps {
        sh '''
                    pytest
                '''
      }
    }

  }
}