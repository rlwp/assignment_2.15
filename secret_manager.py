import boto3

def retrieve_secret(secret_id):
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId=secret_id)
    return response['SecretString']

secret_id = 'your-secret-id'
secret = retrieve_secret(secret_id)
print
