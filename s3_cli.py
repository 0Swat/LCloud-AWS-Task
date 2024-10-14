# s3_cli.py

import os
import boto3
from dotenv import load_dotenv
import re

load_dotenv()

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

BUCKET_NAME = 'developer-task'
PREFIX = 'TIE-rp/'


# 1. List all files in an S3 Bucket
def list_files():
    response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=PREFIX)
    
    if 'Contents' in response:
        for obj in response['Contents']:
            print(obj['Key'])
    else:
        print("No files found.")


if __name__ == '__main__':
    list_files()