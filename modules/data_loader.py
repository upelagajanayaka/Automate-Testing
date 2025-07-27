import csv


class DataLoader:
    def load_csv(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            # Only include rows where 'Amount' is not None and not empty
            return [row for row in reader if row.get('Amount') not in (None, '', ' ')]
