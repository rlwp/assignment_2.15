# assignment_2.15
This is for assignnent 2.5

-	What is needed to authorize your EC2 to retrieve secrets from the AWS Secret Manager?

**1. Create an IAM Role with Necessary Permissions:**
   
•	Go to the IAM Console.

•	Click on "Roles" in the left sidebar.

•	Click on the "Create role" button.

•	Choose "EC2" as the trusted entity.

•	Click on "Next: Permissions."

•	Attach the following policy: SecretsManagerReadWrite

•	Click on "Next: Tags" (you can skip adding tags).

•	Click on "Next: Review."

•	Provide a role name (e.g., EC2SecretsManagerRole).

•	Click on the "Create role" button.

**2.** Attach the IAM Role to Your EC2 Instance:

•	Go to the EC2 Console.

•	Select the instance you want to authorize.

•	Click on "Actions" and select "Instance Settings" -> "Attach/Replace IAM role."

•	Choose the IAM role you created (EC2SecretsManagerRole).

•	Click on the "Update IAM role" button.


**3. Configure Your EC2 Instance to Retrieve Secrets:**

•	Install the AWS CLI and Boto3 library if they are not already installed.

•	Use the following Python code to retrieve the secret from Secrets Manager:


python
import boto3

def retrieve_secret(secret_id):
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId=secret_id)
    return response['SecretString']

secret_id = 'your-secret-id'
secret = retrieve_secret(secret_id)
print


-	Derive the IAM policy (i.e. JSON)?
-	Using the secret name prod/cart-service/credentials, derive a sensible ARN as the specific resource for access

The IAM policy grants read access to the specific secret in AWS Secrets Manager. Here is the JSON representation of the policy:

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue"
            ],
            "Resource": [
                "arn:aws:secretsmanager:<region>:<account-id>:secret:<secret-name>"
            ]
        }
    ]
}


**ARN for the specific secret**

Given the secret name dev/rudyrdsdb/credentials, here is the sensible ARN:

arn:aws:secretsmanager:<region>:<account-id>:secret:prod/cart-service/credentials

Replace <region> with your AWS region (e.g., us-west-1) and <account-id> with your AWS account ID (e.g., 123456789012).

Example policy with Region and Account ID
Here is the example IAM policy with placeholders replaced:
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue"
            ],
            "Resource": [
                "arn:aws:secretsmanager:us-west-1:123456789012:secret:prod/cart-service/credentials"
            ]
        }
    ]
}
This policy allows the entity to retrieve the secret value of dev/rudyrdsdb/secret from AWS Secret Manager.
