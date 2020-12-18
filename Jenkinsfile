pipeline
{
    environment {
        registryCredential = 'dockerhub'
        dockerImage = ''
    }
	options
	{
		timestamps()
	}
	agent none
	stages
	{
		stage('Check scm')
		{
			agent any
			steps
			{
				checkout scm
			}
		} // stage Build
		stage('Build')
		{
			steps
			{
				echo "Building ...${BUILD_NUMBER}"
				echo "Build completed"
			}
		} // stage Build
		stage('Test')
		{
			agent
			{
				docker
				{
					image 'python:3.8.6-slim'
					args '-u=\"root\"'
				}
			}
			steps
			{
				sh 'pip install --no-cache-dir -r ./requirements.txt'
				sh 'python3 Exam.py'
			}
			post
			{

				success
				{
					echo "Application testing successfully completed "
				}
				failure
				{
					echo "Oooppss!!! Tests failed!"
				}
			} // post
		} // stage Test
		stage('Docker Publish')
		{
            agent any
            
            steps {
                echo "Application Publishing"
                checkout scm
                script {
                    def customImage = docker.build("namenus/mexa:${env.BUILD_ID}")
                    docker.withRegistry('',registryCredential )
                    {
                        customImage.push()}
                    }

            }
		} // stage Docker Publish
	} // stages
}
