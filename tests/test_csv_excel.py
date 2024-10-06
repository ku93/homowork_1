import unittest
from unittest.mock import Mock, patch
import pandas as pd
import logging

from src.csv_excel import get_transactions_csv, get_transactions_excel


@patch("src.csv_excel.csv_path")
def test_get_transactions_csv(mock_read_csv):
    mock_transactions = Mock()
    mock_transactions.return_value = pd.DataFrame({"column1": [1, 2, 3]})
    mock_read_csv.return_value = mock_transactions
    tg = get_transactions_csv()
    assert len(tg) == 1000


@patch("src.csv_excel.csv_path")
def test_get_transactions_csv(mock_read_csv):
    mock_transactions = Mock()
    mock_transactions.return_value = pd.DataFrame({"column1": [1, 2, 3]})
    mock_read_csv.return_value = mock_transactions
    tg = get_transactions_excel()
    assert len(tg) == 1000
