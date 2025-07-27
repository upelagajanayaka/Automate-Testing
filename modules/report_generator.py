class ReportGenerator:
    def generate(self, data):
        for month in data:
            print(f"\nSales for {month}:")
            for branch, total in data[month].items():
                print(f"  {branch}: Rs.{total}")
