import boto3
import json

def lambda_handler(event, context):
    # Initialize the SNS client
    sns = boto3.client('sns')
    # Specify your SNS topic ARN
    topic_arn = 'arn:aws:sns:region:account-id:your-topic'

    # Process each record in the event
    for record in event['Records']:
        # Assume the body of the message is a JSON string
        message = json.loads(record['body'])
        print(f"Processing message: {message}")

        # Implement your error handling or anomaly detection logic here
        # For example, check for a specific error condition
        if 'error' in message:
            # Trigger an alert via SNS
            sns.publish(
                TopicArn=topic_arn,
                Message=json.dumps({'default': json.dumps(message)}),
                Subject='Data Processing Error Detected',
                MessageStructure='json'
            )
            print("Alert sent for error:", message['error'])

# Example event format for testing
if __name__ == "__main__":
    test_event = {
        "Records": [
            {
                "body": '{"error": "Sample error message for testing"}'
            }
        ]
    }
    lambda_handler(test_event, None)
