from masks import get_mask_account, get_mask_card_number

inp = input("Введите Ваши реквезиты: ")
name_card = ""
number_card = ""
for i in inp:
    if i.isalpha():
        name_card += i
    elif i == " ":
        name_card += i
    elif i.isdigit():
        number_card += i


def mask_account_card(inp: str) -> str:
    """ "Функция которая умеет обрабатывать информацию как о картах, так и о счетах"""
    if "счет" in inp.lower():
        account = number_card
        rechnung = get_mask_account(account)
        new_rechnung = name_card.title() + " " + rechnung
        return new_rechnung
    else:
        card_number = number_card
        card = get_mask_card_number(card_number)
        new_card = name_card.title() + ": " + card
        return new_card


print(mask_account_card(inp))

data_inp = input("Введите дату: ")


def get_data(data_inp: str) -> str:
    """Функция, которая принимает и преобразует формат даты"""
    data_sp = data_inp.split("T")
    data = data_sp[0].split("-")
    new_data = ".".join(reversed(data))
    return new_data


print(get_data(data_inp))
