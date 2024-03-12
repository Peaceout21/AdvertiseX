import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_s3(parquet_file_path, bucket_name, s3_key):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(parquet_file_path, bucket_name, s3_key)
        print(f"File {parquet_file_path} uploaded to {bucket_name}/{s3_key}")
    except FileNotFoundError:
        print(f"The file {parquet_file_path} was not found.")
    except NoCredentialsError:
        print("Credentials not available.")

def load_to_redshift(s3_path, table_name):
    # This function is a placeholder for the actual Redshift data loading logic.
    # Typically, you would use the Redshift COPY command for this purpose.
    print(f"Loading data from {s3_path} into Redshift table {table_name}")

# Example usage
parquet_file = 'path/to/your/data.parquet'
s3_bucket = 'your-s3-bucket'
s3_key = 'your/s3/key/data.parquet'
upload_to_s3(parquet_file, s3_bucket, s3_key)
load_to_redshift(f"s3://{s3_bucket}/{s3_key}", 'your_redshift_table')
