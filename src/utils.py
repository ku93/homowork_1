import json
import os

from dotenv import load_dotenv

load_dotenv()
absolute_path = os.getenv("absolute_path")


def get_transactions(absolute_path):
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список"""
    try:
        with open(absolute_path, encoding="utf-8") as file:
            data = json.load(file)
            return data if type(data) is list else []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        raise ValueError("Файл не является JSON-файлом")


tr = get_transactions(absolute_path)
print(tr)
