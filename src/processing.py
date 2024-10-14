list_of_dictionary = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(list_of_dictionary: list[dict], state = "EXECUTED"):
    """Принимает список словарей  и опционально параметр, возвращает новый список словарей"""
    list_by_state = []
    for dictionary in list_of_dictionary:
        if dictionary.get("state") == state:
            list_by_state.append(dictionary)
    return list_by_state


# print(filter_by_state(list_of_dictionary))
# print(filter_by_state(list_of_dictionary, "CANCELED"))


def sort_by_date(lists: list[dict], order: bool = True) -> list[dict]:
    """Функция, которая принимает список словарей и необязательный параметр, задающий порядок сортировки"""
    sorted_list = sorted(lists, key=lambda x: x["date"], reverse=order)
    return sorted_list


# print(sort_by_date(list_of_dictionary))
