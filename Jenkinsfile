pipeline{
    agent any
    
    stages{

        stage("Checkout"){
            echo "Pulling code from git"
            git branch :'main', url:"https://github.com/Thusyya-Vardhan/CICD-demo.git"
        }

        stage("Build"){
            echo "Building..."
        }

        stage("Test"){
            echo "Testing..."
        }

        stage("Deploy"){
            echo "Deploying website"
             bat '''
            if not exist C:\\deploy_test mkdir C:\\deploy_test
            xcopy /E /Y * C:\\deploy_test\\
            '''
        }
    }
}