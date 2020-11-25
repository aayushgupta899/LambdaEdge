import boto3
import requests
import time

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

# request for the lambda function
start = time.process_time()
client = boto3.client('lambda', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
response = client.invoke(FunctionName='computePrime')
L = time.process_time() - start
# request for the lambda edge function
start = time.process_time()
url = 'http://d3d51bm7awkuhz.cloudfront.net/download.jfif'
r = requests.get(url, allow_redirects=True)
l = time.process_time() - start
print(f'L : {L}, l : {l}, Roundtrip time : {L+l}')
