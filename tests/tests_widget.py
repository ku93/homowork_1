import pytest

from src.widget import mask_account_card, get_data

@pytest.mark.parametrize(
    'value, expected',
    [
        ('Visa Platinum 7000792289606361', 'Visa Platinum : 7000 79** **** 6361'),
        ('Maestro 7000792289606361', 'Maestro : 7000 79** **** 6361'),
        ('Счет 73654108430135874305', 'Счет **4305')
    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected

@pytest.mark.parametrize(
    'value, expected',
    [
        ('2024-03-11T02:26:18.671407', '11.03.2024')
    ]
)
def test_get_data(value,expected):
    assert  get_data(value)==expected