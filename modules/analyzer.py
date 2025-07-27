class SalesAnalyzer:
    def __init__(self, sales_data):
        self.sales_data = sales_data

    def analyze_monthly_sales(self):
        result = {}
        for row in self.sales_data:
            month = row['Month']
            branch = row['Branch']
            amount = float(row['Amount'])

            if month not in result:
                result[month] = {}
            if branch not in result[month]:
                result[month][branch] = 0

            result[month][branch] += amount

        return result
