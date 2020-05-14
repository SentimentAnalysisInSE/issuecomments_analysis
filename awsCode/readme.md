## Setup

- Create an AWS root user account 
- Using the root user account, create an administrator IAM user and retrieve the IAM user's access keys
(the access keys of the root user could also be used, but AWS recommends using an IAM user for security purposes)
- Store the access keys as environment variables named AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY.
- Install the Python packages "requests" and "pandas"
- Run the following command from the awsCode folder:
  ```
  $ python3 awsDriver.py
  ```

## Source Code Descriptions

##### awsDriver.py 
This file is responsible for reading comments from the Jira.csv file and formatting them into a JSON string. This JSON string is passed to the getSentiment() method as the body of the request to the AWS Comprehend service.
The sentiment labels and scores are aggregated and appended to the csv file in separate columns.

##### postScript.py 
To authenticate the RESTFUL request to the service, this file first generates a Signature Version 4 signature using the access keys. The request returns a JSON string containing sentiment information back to awsDriver.py.
