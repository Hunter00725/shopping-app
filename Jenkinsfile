pipeline {
    agent any
    environment {
        DOCKER_USER = 'your-dockerhub-username'
        IMAGE_NAME  = 'shopping-app'
    }
    stages {
        stage('Checkout Source') {
            steps {
                checkout scm
            }
        }
        
        stage('Build & Tag Docker Images') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_USER}/${IMAGE_NAME}:v1 ./v1"
                    sh "docker build -t ${DOCKER_USER}/${IMAGE_NAME}:v2 ./v2"
                    sh "docker build -t ${DOCKER_USER}/${IMAGE_NAME}:v3 ./v3"
                }
            }
        }
        
        stage('Push Images to DockerHub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER_ENV')]) {
                        sh "echo \$DOCKER_PASS | docker login -u \$DOCKER_USER_ENV --password-stdin"
                        sh "docker push ${DOCKER_USER}/${IMAGE_NAME}:v1"
                        sh "docker push ${DOCKER_USER}/${IMAGE_NAME}:v2"
                        sh "docker push ${DOCKER_USER}/${IMAGE_NAME}:v3"
                    }
                }
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Applies manifests locally inside the cluster environment
                    sh "kubectl apply -f k8s/"
                }
            }
        }
    }
}
