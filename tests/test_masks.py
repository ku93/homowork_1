import pytest

from src.masks import get_mask_account, get_mask_card_number

@pytest.mark.parametrize(
    "value, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("700079228960636", "Номер не может быть меньше 16 цифр"),
        ("70007922896063611", "Номер карты не может быть больше 16 цифр"),
        ("700079ab89606361", "Номер карты не может содержать букв"),
        ("", "Незадан номер карты"),
    ],
)
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize(
    "account, mask_account",
    [
        ("73654108430135874305", "**4305"),
        ("736541084301358743", "**8743"),
        ("7365", "Номер счета не может быть меньше 5 цифр"),
        ("7365410843013587430500", "Номер счета не может быть больше 20 цифр"),
        ("", "Незадан номер счета"),
    ],
)
def test_get_mask_account(account, mask_account):
    assert get_mask_account(account) == mask_account
