lists = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
new_list = []


def filter_by_state(lists, state="EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению"""
    for i in lists:
        if i["state"] == "EXECUTED":
            new_list.append(i)
            lists_st = new_list
    return lists_st


print(filter_by_state(lists))


def sort_by_date(lists, state="EXECUTED") -> list:
    """Функция, которая принимает список словарей и необязательный параметр, задающий порядок сортировки"""
    sorted_list = sorted(lists, key=lambda x: x["date"], reverse=True)
    return sorted_list


print(sort_by_date(lists))
