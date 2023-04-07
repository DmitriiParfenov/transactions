from utils.show_transactions import get_transactions_result
from utils.db_operations import operations_db
from utils.hide_card_number import get_hide_number
import os.path
import pytest


@pytest.fixture
def get_json_main():
    path = os.path.join('.', 'tests', 'file_test_main.json')
    hide_number = operations_db(path)
    result = get_hide_number(hide_number)
    return result


def test_get_transactions_result_sorted_data(get_json_main):
    data_list = get_transactions_result(get_json_main).split('\n')
    data_result = [data_list[0], data_list[4], data_list[8]]
    assert data_result == ['30.06.2018 Перевод организации',
                           '05.05.2018 Перевод с карты на счет',
                           '03.02.2018 Открытие вклада']


def test_get_transactions_result_addresses(get_json_main):
    data_list = get_transactions_result(get_json_main).split('\n')
    data_result = [data_list[1], data_list[5], data_list[9]]
    assert data_result == ['Счет **6952 -> Счет **6702',
                           'MasterCard 9454 78** **** 4532 -> Счет **1351',
                           'Счет **8767']


def test_get_transactions_result_amount_money(get_json_main):
    data_list = get_transactions_result(get_json_main).split('\n')
    data_result = [data_list[2], data_list[6], data_list[10]]
    assert data_result == ['9824.07 USD',
                           '56071.02 руб.',
                           '90297.21 руб.']
