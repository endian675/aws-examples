import urllib.parse
import boto3
import io
import os
import json

s3 = boto3.client('s3')

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    print("Bucket: " + bucket)
    print("Key: " + key)
    
    bytes_buffer = io.BytesIO()
    s3.download_fileobj(Bucket=bucket, Key=key, Fileobj=bytes_buffer)
    byte_value = bytes_buffer.getvalue()
    str_value = byte_value.decode() #python3, default decoding is utf-8
    print(str_value)
