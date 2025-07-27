from modules.data_loader import DataLoader
from modules.analyzer import SalesAnalyzer
from modules.report_generator import ReportGenerator

data_loader = DataLoader()
sales_data = data_loader.load_csv("data/sales_data.csv")

analyzer = SalesAnalyzer(sales_data)
monthly_sales = analyzer.analyze_monthly_sales()

report = ReportGenerator()
report.generate(monthly_sales)
