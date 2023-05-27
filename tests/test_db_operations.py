import json
import os.path

import pytest

from utils.db_operations import operations_db

PATH_1 = os.path.join('../tests', 'file_test.json')
PATH_2 = os.path.join('../tests', 'file_for_test_operation.json')


@pytest.fixture
def get_filled_json_wrong():
    with open(os.path.join('../tests', 'file_test.json'), 'w', encoding='utf-8') as db:
        information = dict(zip(("a", "b"), (1, 2)))
        db.write(json.dumps(information))


@pytest.fixture
def get_empty_json_file():
    with open(os.path.join('../tests', 'file_test.json'), 'w', encoding='utf-8'):
        pass


@pytest.mark.parametrize("expected, way", [('Ошибка, файл не найден', 'example.json'),
                                           ('Проверьте целостность файла', PATH_1)])
def test_operations_db_validate_data(expected, way, get_empty_json_file):
    assert operations_db(way) == expected


def test_operations_db_validate_json_data(get_filled_json_wrong):
    with pytest.raises(ValueError):
        assert operations_db(PATH_1) == "Проверьте корректность данных в файле"


def test_operations_db_sort():
    db = operations_db(PATH_2)
    data_sorted = []
    for elem in db:
        data_sorted.append(elem["date"])
    assert data_sorted == ["18.07.2019", "01.06.2019", "08.02.2019", "05.05.2018"]


def test_operations_db_corrected_state():
    db = operations_db(PATH_2)
    data_corrected = []
    for elem in db:
        if elem['state'] == 'CANCELED':
            data_corrected.append(elem)
    assert data_corrected == []
