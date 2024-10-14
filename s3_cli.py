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

# 2. Upload a local file to a defined location in the bucket
def upload_file(local_file, s3_path_file):
    try:
        s3.upload_file(local_file, BUCKET_NAME, s3_path_file)
    except Exception as e:
        print(f"Error occured: {e}")


if __name__ == '__main__':
    list_files()