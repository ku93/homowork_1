lists = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(lists: list[dict], state="EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует
     указанному значению"""

    new_list = []

    for i in lists:
        if i.get("state") == state:
            new_list.append(i)
    return new_list


print(filter_by_state(lists))
print(filter_by_state(lists, "CANCELED"))


def sort_by_date(lists: list[dict], order: bool = True) -> list[dict]:
    """Функция, которая принимает список словарей и необязательный параметр, задающий порядок сортировки"""
    sorted_list = sorted(lists, key=lambda x: x["date"], reverse=order)
    return sorted_list


print(sort_by_date(lists))
