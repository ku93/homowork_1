import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(r"C:\Users\tkach\OneDrive\Рабочий стол\учебные проекты\скайпро\модуль 2\9.1 Poetry. Оформление кода\homework_1\logs\masks.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая создает маску карты"""
    logger.info("получаем номер карты")
    if card_number == "Незадан номер карты":
        logger.error("Незадан номер карты")
        return "Незадан номер карты"
    elif card_number.isdigit():
        if len(card_number) == 16:
            logger.info("Выводим маску карты")
            masked_card = card_number[:4] + " " + card_number[4:6] + "** ****" + " " + card_number[-4:]
            return masked_card
        elif 0 < len(card_number) < 16:
            logger.error("Номер карты не может быть меньше 16 цифр")
            return "Номер карты не может быть меньше 16 цифр"
        elif len(card_number) > 16:
            logger.error("Номер карты не может быть больше 16 цифр")
            return "Номер карты не может быть больше 16 цифр"
        elif len(card_number) == 0:
            logger.error("Незадан номер карты")
            return "Незадан номер карты"
    else:
        logger.error("Номер карты не может содержать букв")
        return "Номер карты не может содержать букв"


get_mask_card_number("1234567891")


def get_mask_account(account: str) -> str:
    """Функция, которая создает маску счета"""
    logger.info("Получаем номер счета")
    if account == "":
        logger.error("Незадан номер счета")
        return "Незадан номер счета"
    elif account.isdigit():
        if 5 <= len(account) <= 20:
            logger.info("Выводим масук счета")
            return "**" + account[-4:]
        elif len(account) < 5:
            logger.error("Номер счета не может быть меньше 5 цифр")
            return "Номер счета не может быть меньше 5 цифр"
        elif len(account) > 20:
            logger.error("Номер счета не может быть больше 20 цифр")
            return "Номер счета не может быть больше 20 цифр"


get_mask_account("123456789")
