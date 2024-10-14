import re
import collections
import os
from src.utils import get_transactions
from src.csv_excel import get_transactions_csv, get_transactions_excel
from dotenv import load_dotenv

load_dotenv()
absolute_path = os.getenv("absolute_path")

json_file = get_transactions(absolute_path)
csv_file = get_transactions_csv("..//data/transactions.csv")
excel_file = get_transactions_excel("..//data/transactions_excel.xlsx")


def search_transactions(transactions: list[dict], search_string: str) -> list[dict]:
    """Функция, принимает список словарей с данными о банковских операциях и строку поиска, а возвращает
    список словарей, у которых в описании есть данная строка"""
    result = []
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    for transaction in transactions:
        desc = transaction.get('description', "")
        if type(desc) and type(desc) is not str:
            pass
        elif re.search(pattern,desc):
            result.append(transaction)
    return result

# t = search_transactions(excel_file, 'Перевод организации')
# print(t)

def get_count_transactions(transactions: list[dict], user_categories: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций,
а возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    descriptions = []
    category = []
    count = []
    for transaction in transactions:
        descriptions.append(transaction.get("description"))

    for cat in user_categories:
        cat.lower()
        category.append(cat)

        for description in descriptions:
            d=str(description)
            if cat.lower() == d.lower():
                count.append(cat)
    return dict(collections.Counter(count))

# g = get_count_transactions(excel_file, ["Перевод организации", "открытие вклада", "Перевод со счета на счет"])
# print(g)