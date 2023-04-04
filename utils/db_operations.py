import json
import os
import datetime as dt


def operations_db(path):
    """
    Функция в качестве аргумента получает путь к json-файлу с банковскими операциями.
    Файл должен находиться в пакете utils. Если файл пустой, то функция вернет оповещающую строку
    о необходимости проверки файла. Если в файле некорректные данные, то функция возбудит исключение ValueError.
    Функция проверяет корректность ключей в файле, подразумевается, что если 'state' = 'EXECUTED', то файл
    содержит корректные данные.
    Функция возвращает список с отсортированными в порядке убывания банковскими операциями в размере 5 элементов
    :param path: str
    :return: list
    """
    log_list = []
    latest_operation = []
    # Проверка корректности нахождения файла
    if not os.path.exists(path):
        return f'Ошибка, файл не найден'
    # Проверка целостности файла
    try:
        with open(path, 'r', encoding='utf-8') as db_file:
            db_dict = json.load(db_file)
            # Проверка корректности данных в файле
            if not isinstance(db_dict, list):
                raise ValueError("Проверьте корректность данных в файле")

            for elem in db_dict:
                try:
                    latest_operation.append(elem) if elem['state'] == 'EXECUTED' else ...
                except KeyError:
                    log_list.append(f'Элемент = {elem}, Тип = {type(elem)}')

            latest_operation.sort(key=lambda x: x['date'], reverse=True)

            for elem in latest_operation:
                elem['date'] = dt.datetime.fromisoformat(elem['date']).strftime('%d.%m.%Y')
    except json.JSONDecodeError:
        return f'Проверьте целостность файла'

    return latest_operation[:5]
