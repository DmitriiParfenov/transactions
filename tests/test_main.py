from scr.main import main
from utils.db_operations import operations_db
from utils.hide_card_number import get_hide_number
from utils.show_transactions import get_transactions_result
import os.path
import pytest


@pytest.fixture
def get_json_main():
    path = os.path.join('.', 'tests', 'file_test_main.json')
    result = main(path)
    return result.split('\n')


def test_main_with_from(get_json_main):
    data_list = get_json_main
    variant = data_list[:3]
    assert variant == ['30.06.2018 Перевод организации',
                       'Счет **6952 -> Счет **6702',
                       '9824.07 USD']


def test_main_without_from(get_json_main):
    data_list = get_json_main
    variant = data_list[8:]
    assert variant == ['03.02.2018 Открытие вклада',
                       'Счет **8767',
                       '90297.21 руб.',
                       '', '']
