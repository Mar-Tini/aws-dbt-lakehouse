from pathlib import Path
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    "s3",
    endpoint_url=os.getenv("AWS_ENDPOINT_URL"),
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1",
)

bucket = os.getenv("AWS_BUCKET")
key = os.getenv("S3_KEY")

local_file = Path(os.getenv(
    "LOCAL_FILE",
    "./data/processed/data_clean.csv"
))

# Ensure the local directory exists
local_file.parent.mkdir(parents=True, exist_ok=True)

print(f"Downloading s3://{bucket}/{key}")

response = s3.get_object(Bucket=bucket, Key=key)

with open(local_file, "wb") as f:
    f.write(response["Body"].read())

print("OK ->", local_file)