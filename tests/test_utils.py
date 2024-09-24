import json
import os

from dotenv import load_dotenv

from src.utils import get_transactions

load_dotenv()
absolute_path = os.getenv('absolute_path')

def test_get_transactions_1():
    result=get_transactions(absolute_path)
    assert result==get_transactions(absolute_path)

def test_get_transactions_2():
    result=get_transactions("obj.json")
    assert result == []

def test_get_transactions_3():
    try:
        result=get_transactions("'")
    except ValueError:
        assert result == 'Файл не является JSON-файлом'