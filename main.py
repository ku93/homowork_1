import os
from src.widget import get_data, mask_account_card
from src.utils import get_transactions
from src.csv_excel import get_transactions_csv, get_transactions_excel
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.func_re import search_transactions, get_count_transactions
from dotenv import load_dotenv

load_dotenv()
absolute_path = os.getenv("absolute_path")


def main():
    print("������! ����� ���������� � ��������� ������ � ����������� ������������.")
    print("�������� ����������� ����� ����:")
    print("1. �������� ���������� � ����������� �� JSON-�����")
    print("2. �������� ���������� � ����������� �� CSV-�����")
    print("3. �������� ���������� � ����������� �� XLSX-�����")

    choice = input("������������: ")
    lists = ["1", "2", "3"]
    attempts_left = 3

    while choice not in lists and attempts_left > 0:
        attempts_left -= 1
        print(f"������������ �����. ����������, ���������� �����. �������� ������� {attempts_left}")
        choice = input("������������: ")

    if attempts_left == 0:
        print("������������ ��� �������. ��������� ��������� ������")
        return

    if choice == '1':
        sort = get_transactions(absolute_path)
        print("��� ��������� ������ JSON-����")
    elif choice == '2':
        sort = get_transactions_csv("..//data/transactions.csv")
        print("��� ��������� ������ CSV-����")
    elif choice == '3':
        sort = get_transactions_excel("..//data/transactions_excel.xlsx")
        print("��� ��������� ������ XLSX-����")

    print("""������� ������, �� �������� ���������� ��������� ����������.
��������� ��� ���������� �������: EXECUTED, CANCELED, PENDING""")
    user_input = input("������������: ")

    if user_input.strip().upper() == "EXECUTED":
        sort = filter_by_state(sort, "EXECUTED")
        print("�������� ������������� �� ������� 'EXECUTED'")
    elif user_input.strip().upper() == "CANCELED":
        sort = filter_by_state(sort, "CANCELED")
        print("�������� ������������� �� ������� 'CANCELED'")
    elif user_input.strip().upper() == "PENDING":
        sort = filter_by_state(sort, "PENDING")
        print("�������� ������������� �� ������� 'PENDING'")
    else:
        print(f'������ �������� "{user_input}" ����������')

    print("������������� �������� �� ����? ��/���")
    date = input("������������: ")
    if date.lower() == "��".lower():
        print("������������� �� ����������� ��� �� ��������? (�� �����������/�� ��������)")
        t = input("������������: ")
        if t.lower() == "�� �����������".lower():
            sort= sort_by_date(sort, True)
        else:
            sort = sort_by_date(sort, False)
    else: sort

    print("�������� ������ �������� ���������? ��/���")
    currency_filter = input("������������: ").strip().lower()

    if currency_filter == "��":
        sort = filter_by_currency(sort, "RUB")

    print("������������� ������ ���������� �� ������������� ����� � ��������? ��/���")
    description_filter = input("������������: ").strip().lower()

    if description_filter == "��":
        search = input("��������� ������? (�������� ������/ ������� �����������/ ������� � ����� �� �����): ").strip()
        sort = search_transactions(sort, search)

    print("������������ �������� ������ ����������...")
    if list(sort) != 0:
        print(f"����� ���������� �������� � �������: {len(sort)}")
        for transaction in sort:
            date = get_data(transaction["date"])
            description = transaction["description"]
            card_to = mask_account_card(transaction["to"])
            try:
                amount = round(float(transaction.get("operationAmount").get("amount")))
                name = transaction.get("operationAmount").get("currency").get("name")
            except AttributeError:
                amount = round(float(transaction.get("amount")))
                name = transaction.get("currency_name")
            if transaction.get("from") is not None and str(transaction.get("from")) != "nan":
                card_from = mask_account_card(str(transaction.get("from")))
                print(f"{date} {description}\n{card_from} -> {card_to}\n�����: {amount} {name}\n\n")
            else:
                print(f"{date} {description}\n{card_to}\n�����: {amount} {name}\n\n")

    else:
        print("�� ������� �� ����� ����������, ���������� ��� ���� ������� ����������.")


g = main()
print(g)

