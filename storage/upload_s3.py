import boto3 # type: ignore

s3 = boto3.client(
    "s3",
    endpoint_url="http://aws-local:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1"
)

bucket = "ecommerce-lake"

# create bucket
s3.create_bucket(Bucket=bucket)

# upload file
s3.upload_file(
    "data/raw/data.csv",
    bucket,
    "raw/data.csv"
)

print("upload done ... ")