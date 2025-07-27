import sys
import os

# Add the parent directory to sys.path to import modules
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


def test_full_data_analysis_integration(tmp_path):
    from modules.data_loader import DataLoader
    from modules.analyzer import SalesAnalyzer
    from modules.report_generator import ReportGenerator

    # --- Step 1: Create a temporary CSV file ---
    csv_content = "Month,Branch,Amount\nJanuary,Colombo,500\nJanuary,Kandy,300\nJanuary,Colombo,200"
    temp_file = tmp_path / "test_sales.csv"
    temp_file.write_text(csv_content)

    # --- Step 2: Load data ---
    loader = DataLoader()
    data = loader.load_csv(str(temp_file))

    # --- Step 3: Analyze data ---
    analyzer = SalesAnalyzer(data)
    result = analyzer.analyze_monthly_sales()

    # --- Step 4: Verify integration result ---
    assert result['January']['Colombo'] == 700.0
    assert result['January']['Kandy'] == 300.0

    # (Optional) Call report.generate(result) to see output
    report = ReportGenerator()
    report.generate(result)
