import csv

def process_csv(file_path):
    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # Process each row
            print(row)

# Example usage
process_csv('path/to/your/csv/file.csv')
