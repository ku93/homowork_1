import os

import requests
from src.utils import get_transactions
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
absolute_path = os.getenv("absolute_path")

ap = get_transactions(absolute_path)

def convert(transactions):
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
    тип данных — float"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"].lower() == "RUB".lower():
            return float(transaction["operationAmount"]["amount"])
        elif transaction["operationAmount"]["currency"]["code"] == "USD":

            amount = transaction["operationAmount"]["amount"]
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=rub&from=USD&amount={amount}"
            headers = {"apikey": f"{API_KEY}"}
            response = requests.get(url, headers=headers)
            result = response.json()
            return float(round(result["result"], 2))
        elif transaction["operationAmount"]["currency"]["code"] == []:
            return []
        elif transaction["operationAmount"]["currency"]["code"] is None:
            return []


operation = {"operationAmount": {"amount": "25780.71", "currency": {"name": "руб.", "code": "USD"}}}

# r = convert(ap)
# print(r)
