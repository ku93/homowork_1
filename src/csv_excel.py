import pandas as pd
import logging

logger = logging.getLogger("csv_excel")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/csv_excel.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def reader_csv(file):
    """Считывание финансовых операций из CSV-файла. Возвращает список словарей с транзакциями"""
    transactions = pd.read_csv(file, delimiter=";")
    return transactions.to_dict(orient="records")


def reader_excel(file):
    """Считывание финансовых операций из XLSX-файла. Возвращает список словарей с транзакциями"""
    transactions = pd.read_excel(file)
    return transactions.to_dict(orient="records")