from google.cloud import bigquery

def load_to_bigquery(parquet_file_path, dataset_id, table_id):
    client = bigquery.Client()
    table_ref = client.dataset(dataset_id).table(table_id)
    job_config = bigquery.LoadJobConfig(source_format=bigquery.SourceFormat.PARQUET)
    with open(parquet_file_path, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_ref, job_config=job_config)

    job.result()  # Waits for the job to complete
    print(f"Loaded {job.output_rows} rows into {dataset_id}:{table_id} from {parquet_file_path}")

# Example usage
parquet_file = 'path/to/your/data.parquet'
dataset = 'your_dataset'
table = 'your_table'
load_to_bigquery(parquet_file, dataset, table)
