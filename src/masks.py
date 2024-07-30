def get_mask_card_number(card_number: str) -> str:
    """Функция, которая создает маску карты"""
    masked_card = card_number[:4] + " " + card_number[4:6] + "** ****" + " " + card_number[-4:]
    return masked_card


def get_mask_account(account: str) -> str:
    """Функция, которая создает маску счета"""
    stars = 2 * "*"
    mask_account = stars + account[2:]
    return mask_account
