import boto3
from collections.abc import Mapping,Sequence

#set the client
ecr_client=boto3.client('ecr')

#create the repo
repository_name="my-cloud-native-repo"
response=ecr_client.create_repository(repositoryName=repository_name)

#it will store the value of the repository Uri
repository_uri=response["repository"]["repositoryUri"]
print(repository_uri)

#repository created 
