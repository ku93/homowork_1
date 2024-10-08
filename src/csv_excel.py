import pandas as pd
import logging

logger = logging.getLogger("csv_excel")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/csv_excel.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

csv_path = "..//data/transactions.csv"


def get_transactions_csv():
    """Функция, которая принимает на вход путь к csv"""
    try:
        logger.info("Открываем файл csv")
        transactions = pd.read_csv(csv_path)
        return transactions
    except FileNotFoundError as ex:
        logger.error(f"Произошла ошибка: файл не найден - {ex}")
        return pd.DataFrame()  # Возвращаем пустой DataFrame вместо списка
    except pd.errors.ParserError as ex:
        logger.error(f"Произошла ошибка при разборе csv - {ex}")
        return pd.DataFrame()  # Возвращаем пустой DataFrame вместо списка
    except Exception as ex:
        logger.error(f"Произошла непредвиденная ошибка - {ex}")
        return pd.DataFrame()  # Возвращаем пустой DataFrame вместо списка


tg = get_transactions_csv()
print(tg.head())

excel_path = "../data/transactions_excel.xlsx"


def get_transactions_excel():
    """Функция, которая принимает на вход путь к excel"""
    try:
        logger.info("Открываем файл excel")
        excel_data = pd.read_excel(excel_path)
        return excel_data
    except FileNotFoundError as ex:
        logger.error(f"Произошла ошибка: файл не найден - {ex}")
        return pd.DataFrame()  # Возвращаем пустой DataFrame вместо списка
    except pd.errors.ParserError as ex:
        logger.error(f"Произошла ошибка при разборе csv - {ex}")
        return pd.DataFrame()  # Возвращаем пустой DataFrame вместо списка
    except Exception as ex:
        logger.error(f"Произошла непредвиденная ошибка - {ex}")
        return pd.DataFrame()  # Возвращаем пустой DataFrame вместо списка


ex = get_transactions_excel()
print(ex.head())
