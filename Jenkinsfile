pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/arzharch/Snake-Game'
            }
        }

        stage('Build') {
            steps {
                echo 'Build step (nothing to build yet)'
            }
        }

        stage('Test') {
            steps {
                echo 'No tests yet — skipping for now'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}
