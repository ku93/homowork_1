import json
import logging
import os

from dotenv import load_dotenv

load_dotenv()
absolute_path = os.getenv("absolute_path")

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions(absolute_path):
    """Функция которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых
    транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список"""
    try:
        logger.info("Открываем файл JSON файл")

        with open(absolute_path, encoding="utf-8") as file:
            data = json.load(file)
            return data

    except FileNotFoundError as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return []
    except json.JSONDecodeError as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return []


# tr = get_transactions(absolute_path)
# print(tr)
