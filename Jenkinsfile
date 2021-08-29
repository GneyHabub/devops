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
                    apt-get install sudo -y
                    sudo python -m pip install --upgrade pip
                    sudo pip install -r app_python/requirements.txt
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