import fastavro

def process_avro(file_path):
    with open(file_path, 'rb') as avro_file:
        reader = fastavro.reader(avro_file)
        for record in reader:
            # Process each record
            print(record)

# Example usage
process_avro('path/to/your/avro/file.avro')
