import unittest
from modules.analyzer import SalesAnalyzer


class TestSalesAnalyzer(unittest.TestCase):
    def test_analyze_monthly_sales(self):
        test_data = [
            {'Month': 'January', 'Branch': 'Colombo', 'Amount': '500'},
            {'Month': 'January', 'Branch': 'Colombo', 'Amount': '200'},
            {'Month': 'January', 'Branch': 'Kandy', 'Amount': '300'}
        ]
        analyzer = SalesAnalyzer(test_data)
        result = analyzer.analyze_monthly_sales()

        self.assertEqual(result['January']['Colombo'], 700.0)
        self.assertEqual(result['January']['Kandy'], 300.0)


if __name__ == '__main__':
    unittest.main()
