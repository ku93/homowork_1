from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_USD(transactions):
    exp = filter_by_currency(transactions, "USD")
    result = list(exp)
    assert result == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


def test_filter_by_currency_EUR(transactions):
    exp = filter_by_currency(transactions, "EUR")
    result = list(exp)
    assert result == [
        {
            "id": 142264000,
            "state": "EXECUTED",
            "date": "2010-06-04T23:20:05.206878",
            "operationAmount": {"amount": "714.00", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод с карты на карту",
            "from": "Счет 19708645243227258000",
            "to": "Счет 75651667383060284111",
        }
    ]


def test_filter_by_currency_PU(transactions):
    exp = filter_by_currency(transactions, "")
    result = list(exp)
    assert result == []


def test_filter_by_currency_no(transactions):
    exp = filter_by_currency(transactions, "USDT")
    result = list(exp)
    assert result == []


def test_transaction_descriptions(transactions):
    exp = transaction_descriptions(transactions)
    result = list(exp)
    assert result == ["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"]


def test_card_number_generator():
    start = "0000 0000 0000 0001"
    end = "0000 0000 0000 0010"
    expected_output = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
        "0000 0000 0000 0006",
        "0000 0000 0000 0007",
        "0000 0000 0000 0008",
        "0000 0000 0000 0009",
        "0000 0000 0000 0010",
    ]
    generated_output = list(card_number_generator(start, end))
    assert generated_output == expected_output

    start = "0000 0000 0000 0001"
    end = "0000 0000 0000 0001"
    expected_output = ["0000 0000 0000 0001"]
    generated_output = list(card_number_generator(start, end))
    assert generated_output == expected_output

    start = "1234 5678 1234 5678"
    end = "1234 5678 1234 5680"
    expected_output = [
        "1234 5678 1234 5678",
        "1234 5678 1234 5679",
        "1234 5678 1234 5680",
    ]
    generated_output = list(card_number_generator(start, end))
    assert generated_output == expected_output

    start = "9999 9999 9999 9998"
    end = "9999 9999 9999 9999"
    expected_output = [
        "9999 9999 9999 9998",
        "9999 9999 9999 9999",
    ]
    generated_output = list(card_number_generator(start, end))
    assert generated_output == expected_output
