pipeline{
    agent any
    
    stages{

        stage("Checkout"){
            steps{
            echo "Pulling code from git"
            git branch :'master', url:"https://github.com/Thusyya-Vardhan/CICD-demo.git"
        }
    }

        stage("Build"){
            steps{
            echo "Building..."
        }
    }

        stage("Test"){
            steps{
            echo "Testing..."
        }
    }

        stage("Deploy"){
            steps{
            echo "Deploying website"
             bat '''
            if not exist C:\\deploy_test mkdir C:\\deploy_test
            xcopy /E /Y * C:\\deploy_test\\
            '''
        }
    }
    }
}