import pytest
import json
import os.path

PATH = os.path.join('tests', 'tests_db_operation', 'file_test.json')


@pytest.fixture
def get_filled_json_wrong():
    with open(PATH, 'w', encoding='utf-8') as db:
        information = dict(zip(("a", "b"), (1, 2)))
        db.write(json.dumps(information))


@pytest.fixture
def get_empty_json_file():
    with open(PATH, 'w', encoding='utf-8'):
        pass

