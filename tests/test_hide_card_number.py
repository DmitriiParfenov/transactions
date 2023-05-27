import os.path

import pytest

from utils.db_operations import operations_db
from utils.hide_card_number import get_hide_number


@pytest.fixture
def get_json_main():
    result = operations_db(os.path.join('../tests', 'file_test_main.json'))
    return result


def test_get_hide_number_to_account(get_json_main):
    data_list = get_hide_number(get_json_main)
    secret_account = []
    for elem in data_list:
        secret_account += [f'{elem["to"]}']
    assert secret_account == ['Счет **6702', 'Счет **1351', 'Счет **8767']


def test_get_hide_number_from_account(get_json_main):
    data_list = get_hide_number(get_json_main)
    card_transaction = []
    for elem in data_list:
        if elem.get("from"):
            card_transaction += [f'{elem["from"]} -> {elem["to"]}']
    assert card_transaction == ['Счет **6952 -> Счет **6702', 'MasterCard 9454 78** **** 4532 -> Счет **1351']


def test_get_hide_number_description(get_json_main):
    data_list = get_hide_number(get_json_main)
    description = []
    for elem in data_list:
        description += [f'{elem["description"]}']
    assert description == ['Перевод организации', 'Перевод с карты на счет', 'Открытие вклада']


def test_get_hide_number_validate_data():
    assert get_hide_number([1, 2, 3]) == f'Проверьте данные в файле. ' \
                                         f'Подразумевается вызов функции operations_db перед исполнением get_hide_number'
