import os
import pandas as pd
from dotenv import load_dotenv

from src.utils import get_transactions, get_transactions_csv

load_dotenv()
absolute_path = os.getenv("absolute_path")


def test_get_transactions_1():
    result = get_transactions(absolute_path)
    assert result == get_transactions(absolute_path)


def test_get_transactions_2():
    result = get_transactions("obj.json")
    assert result == []


def test_get_transactions_3():
    try:
        result = get_transactions("'")
    except ValueError:
        assert result == []
