import sys
import os

# Add the parent directory to sys.path so we can import from 'modules'
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


def test_loader_with_mocked_file(mocker):
    # Mock CSV data
    mock_csv = "Month,Branch,Amount\nJanuary,Colombo,1000"

    # Replace open() with mock_open
    mocker.patch("builtins.open", mocker.mock_open(read_data=mock_csv))

    # Import and run DataLoader
    from modules.data_loader import DataLoader
    loader = DataLoader()
    data = loader.load_csv("fake.csv")  # this file doesn't need to exist

    assert data[0]['Month'] == 'January'
    assert data[0]['Branch'] == 'Colombo'
    assert data[0]['Amount'] == '1000'
