import boto3

def lambda_handler(event, context):
    # Example error handling logic
    print("Error detected:", event)
    # Logic to process the error event
    # For example, sending a notification via SNS
    sns = boto3.client('sns')
    sns.publish(
        TopicArn='arn:aws:sns:region:account-id:YourSNSTopic',
        Message='An error has been detected and logged.',
        Subject='Error Notification'
    )

# Note: Replace 'YourSNSTopic' with your actual SNS topic ARN
