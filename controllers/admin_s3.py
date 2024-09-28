import boto3
from keys import ACCESS_KEY, SECRET_KEY
bucket_name = "bucket-aws-cris-1"

def connectionS3():
    session_aws = boto3.Session(ACCESS_KEY,SECRET_KEY)
    session_s3 = session_aws.resource('s3')
    return session_s3

def get_file():
    session_s3 = connectionS3()
    bucket_project = session_s3.Bucket(bucket_name)
    bucket_objects = bucket_project.objects.all()
    for obj in bucket_objects:
        print(obj.key)
    print(bucket_objects)

get_file()
