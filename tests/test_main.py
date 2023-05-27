import os.path

import pytest

from main import main


@pytest.fixture
def get_json_main():
    path = os.path.join('../tests', 'file_test_main.json')
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
