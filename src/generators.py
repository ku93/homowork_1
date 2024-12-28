from src.csv_excel import get_transactions_csv

csv_f = get_transactions_csv("..//data/transactions.csv")


def filter_by_currency(transactions: list[dict], currency_code: str) -> list[dict]:
    """Функция, которая возвращает список транзакций, где валюта операции соответствует заданной."""
    filtered_transactions = []
    for transaction in transactions:
        try:
            if transaction["operationAmount"]["currency"]["code"] == currency_code:
                filtered_transactions.append(transaction)
                return filtered_transactions
        except KeyError:
            if transaction["currency_code"] == currency_code:
                filtered_transactions.append(transaction)
                return filtered_transactions


# f = filter_by_currency(csv_f, "RUB")
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
