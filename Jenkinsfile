pipeline {
  agent any
  environment {
    NS = "${env.BRANCH_NAME == 'main' ? 'produccion' : 'pruebas'}"
    NODEPORT = "${env.BRANCH_NAME == 'main' ? '30080' : '30081'}"
  }
  stages {
    stage('Build imagen') {
      steps {
        sh '''
          eval $(minikube docker-env)
          docker build -t miapp:${BUILD_NUMBER} -t miapp:latest .
        '''
      }
    }
    stage('Deploy en Kubernetes') {
      steps {
        sh '''
          kubectl create namespace $NS --dry-run=client -o yaml | kubectl apply -f -
          sed "s/NODEPORT_PLACEHOLDER/$NODEPORT/" k8s/deployment.yaml | kubectl apply -n $NS -f -
          kubectl rollout restart deployment/miapp -n $NS
          kubectl rollout status deployment/miapp -n $NS
        '''
      }
    }
  }
}
