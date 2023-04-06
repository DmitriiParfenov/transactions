from scr.main import main


def test_main_sorted_data():
    data_list = main("file_test_main.json").split('\n')
    data_result = [data_list[0], data_list[4]]
    assert data_result == ['05.05.2018 Перевод с карты на счет', '03.02.2018 Открытие вклада']


def test_main_to_account():
    data_list = main("file_test_main.json").split('\n')
    secret_account = data_list[5]
    assert secret_account == 'Счет **8767'


def test_main_card_transaction():
    data_list = main("file_test_main.json").split('\n')
    card_transaction = data_list[1]
    assert card_transaction == 'MasterCard 9454 78** **** 4532 -> Счет **1351'


def test_main_description():
    data_list = main("file_test_main.json").split('\n')
    description = data_list[0][11:]
    assert description == 'Перевод с карты на счет'


def test_main_amount_money():
    data_list = main("file_test_main.json").split('\n')
    amount_money = data_list[6]
    assert amount_money == '90297.21 руб.'


def test_main_with_from():
    data_list = main("file_test_main.json").split('\n')
    variant = data_list[:3]
    assert variant == ['05.05.2018 Перевод с карты на счет',
                       'MasterCard 9454 78** **** 4532 -> Счет **1351',
                       '56071.02 руб.']


def test_main_without_from():
    data_list = main("file_test_main.json").split('\n')
    variant = data_list[4:]
    assert variant == ['03.02.2018 Открытие вклада',
                       'Счет **8767',
                       '90297.21 руб.',
                       '', '']
