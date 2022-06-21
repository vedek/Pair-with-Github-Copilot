%AWS lambda function with S3 trigger to textract text from an image
%and upload it to S3 bucket
%https://www.upwork.com/jobs/~013a2f113b96e07941?link=title&n=2&frkscc=eJzH6yCCCTeG
import json
import boto3

def lambda_handler(event, context):

    bucket="bucket"
    document="document"
    client = boto3.client('textract')



    #process using S3 object
    response = client.detect_document_text(
        Document={'S3Object': {'Bucket': bucket, 'Name': document}})

    #Get the text blocks
    blocks=response['Blocks']
    %upload to S3 bucket
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket, Key=document, Body=json.dumps(blocks))
    
    
    return {
        'statusCode': 200,
        'body': json.dumps(blocks)
    }
               
            
