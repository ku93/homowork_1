import os
from src.widget import get_data, mask_account_card
from src.utils import get_transactions
from src.csv_excel import reader_csv, reader_excel
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.func_re import search_transactions, get_count_transactions
from dotenv import load_dotenv

load_dotenv()
absolute_path = os.getenv("absolute_path")


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")
    lists = ["1", "2", "3"]
    attempts_left = 3

    while choice not in lists and attempts_left > 0:
        attempts_left -= 1
        print(f"Некорректный выбор. Пожалуйста, попробуйте снова. Осталось попыток {attempts_left}")
        choice = input("Пользователь: ")

    if attempts_left == 0:
        print("Использованы все попытки. Программа завершает работу")
        return

    if choice == '1':
        sort = get_transactions(absolute_path)
        print("Для обработки выбран JSON-файл")
    elif choice == '2':
        sort = reader_csv("..//data/transactions.csv")
        print("Для обработки выбран CSV-файл")
    elif choice == '3':
        sort = reader_excel("..//data/transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл")

    print("""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
    user_input = input("Пользователь: ")

    if user_input.strip().upper() == "EXECUTED":
        sort = filter_by_state(sort, "EXECUTED")
        print("Операции отфильтрованы по статусу 'EXECUTED'")
    elif user_input.strip().upper() == "CANCELED":
        sort = filter_by_state(sort, "CANCELED")
        print("Операции отфильтрованы по статусу 'CANCELED'")
    elif user_input.strip().upper() == "PENDING":
        sort = filter_by_state(sort, "PENDING")
        print("Операции отфильтрованы по статусу 'PENDING'")
    else:
        print(f'Статус операции "{user_input}" недоступен')

    print("Отсортировать операции по дате? Да/Нет")
    date = input("Пользователь: ")
    if date.lower() == "Да".lower():
        print("Отсортировать по возрастанию или по убыванию? (по возрастанию/по убыванию)")
        t = input("Пользователь: ")
        if t.lower() == "по возрастанию".lower():
            sort= sort_by_date(sort, True)
        else:
            sort = sort_by_date(sort, False)
    else: sort

    print("Выводить только рублевые тразакции? Да/Нет")
    currency_filter = input("Пользователь: ").strip().lower()

    if currency_filter == "да":
        sort = filter_by_currency(sort, "RUB".lower())

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    description_filter = input("Пользователь: ").strip().lower()

    if description_filter == "да":
        search = input("Категория поиска? (Открытие вклада/ Перевод организации/ Перевод с карты на карту): ").strip()
        sort = search_transactions(sort, search)

    return sort

g = main()
print(g)

