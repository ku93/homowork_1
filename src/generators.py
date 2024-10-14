transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 142264000,
        "state": "EXECUTED",
        "date": "2010-06-04T23:20:05.206878",
        "operationAmount": {"amount": "714.00", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод с карты на карту",
        "from": "Счет 19708645243227258000",
        "to": "Счет 75651667383060284111",
    },
]


def filter_by_currency(transactions: list[dict], currency_code: str) -> list[dict]:
    """Функция, которая возвращает список транзакций, где валюта операции соответствует заданной."""
    filtered_transactions = []
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            filtered_transactions.append(transaction)
            return filtered_transactions
# f = filter_by_currency(transactions, "RUB")
# print(f)


def transaction_descriptions(transactions: list[dict]) -> list[dict]:
    "Генератор,  который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."
    for transaction in transactions:
        yield transaction["description"]


# descriptions = transaction_descriptions(transactions)
# for i in range(3):
#     print(next(descriptions))


def card_number_generator(start: int, end) -> int:
    """Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX."""
    start_int = int(start.replace(" ", ""))
    end_int = int(end.replace(" ", ""))

    for number in range(start_int, end_int + 1):
        card_number = f"{number:016d}"
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number

#
# start = "0000 0000 0000 0001"
# end = "0000 0000 0000 0010"
#
# for card_number in card_number_generator(start, end):
#     print(card_number)
