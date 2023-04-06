from utils.db_operations import operations_db
import pytest
import os.path

PATH_file1 = os.path.join('tests_db_operation', 'file_test.json')
PATH_file2 = os.path.join('tests_db_operation', 'file_for_test_operation.json')


@pytest.mark.parametrize("expected, way", [('Ошибка, файл не найден', os.path.join('utils', 'example.json')),
                                           ('Проверьте целостность файла', 'file_test.json')])
def test_operations_db_validate_data(expected, way, get_empty_json_file):
    assert operations_db(way) == expected


def test_operations_db_validate_json_data(get_filled_json_wrong):
    with pytest.raises(ValueError):
        assert operations_db('file_test.json') == "Проверьте корректность данных в файле"


def test_operations_db_sort():
    db = operations_db('file_for_test_operation.json')
    data_sorted = []
    for elem in db:
        data_sorted.append(elem["date"])
    assert data_sorted == ["18.07.2019", "01.06.2019", "08.02.2019", "05.05.2018"]


def test_operations_db_corrected_state():
    db = operations_db('file_for_test_operation.json')
    data_corrected = []
    for elem in db:
        if elem['state'] == 'CANCELED':
            data_corrected.append(elem)
    assert data_corrected == []

