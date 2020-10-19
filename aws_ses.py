import boto3
from botocore.exceptions import ClientError
import numpy as np
import pandas as pd

# Sends emails from a CSV
# CSV has four headers: email, firstName, message, messagePlain
# message is formatted with html and includes the whole email
# messagePlain is formatted in plain text and includes the whole email

def sendEmail(RECIPIENT, BODY_HTML, BODY_TEXT, SUBJECT):
    try:
        # Provide the contents of the email.
        # Replace CcAddresses with your own
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
                'CcAddresses': [
                    "team@studybuddies.ai"
                ]
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
    # Display an error if something goes wrong.	
    except ClientError as e:
        print("")
        print("-----")
        print(e.response['Error']['Message'])
        print(RECIPIENT)
        print("-----")
        print("")
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
        print(RECIPIENT)


# Replace with your "From" address.
# This address must be verified with Amazon SES.
SENDER = "Varun Jindal <my_email@domain.edu>"

# If necessary, replace us-east-2 with the AWS Region you're using for Amazon SES.
AWS_REGION = "us-east-2"

# The character encoding for the email.
CHARSET = "UTF-8"

# Create a new SES resource and specify a region.
client = boto3.client('ses',region_name=AWS_REGION)

# replace this with your own CSV
students = pd.read_csv('./your_csv_goes_here.csv').to_numpy()

# this is the loop that interates over the CSV and sends emails
for student in students:
    sendEmail(student[0], student[2], student[3], "Hey " + student[1] + ", your long awaited matches are finally here") 

