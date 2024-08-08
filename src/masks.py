def get_mask_card_number(card_number: str) -> str:
    """Функция, которая создает маску карты"""
    if card_number=='':
        return 'Незадан номер карты'
    elif card_number.isdigit():
        if len(card_number) ==16:
            masked_card = card_number[:4] + " " + card_number[4:6] + "** ****" + " " + card_number[-4:]
            return masked_card
        elif 0<len(card_number) < 16:
            return 'Номер карты не может быть меньше 16 цифр'
        elif len(card_number) > 16:
            return 'Номер карты не может быть больше 16 цифр'
        elif len(card_number)==0:
            return 'Незадан номер карты'
    else:
        return 'Номер карты не может содержать букв'



def get_mask_account(account: str) -> str:
    """Функция, которая создает маску счета"""
    if account=='':
        return 'Незадан номер счета'
    elif account.isdigit():
        if 5<=len(account)<=20:
            return '**'+account[-4:]
        elif len(account)<5:
            return 'Номер счета не может быть меньше 5 цифр'
        elif len(account)>20:
            return 'Номер счета не может быть больше 20 цифр'
