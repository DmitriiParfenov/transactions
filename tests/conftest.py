import pytest
import json


@pytest.fixture
def get_filled_json_wrong():
    with open('file_test.json', 'w', encoding='utf-8') as db:
        information = dict(zip(("a", "b"), (1, 2)))
        db.write(json.dumps(information))


@pytest.fixture
def get_empty_json_file():
    with open('file_test.json', 'w', encoding='utf-8'):
        pass
