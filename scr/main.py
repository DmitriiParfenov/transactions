from utils.db_operations import operations_db
from utils.hide_card_number import get_hide_number
from utils.show_transactions import get_transactions_result
import os.path

# Объявление текущего пути к файлу с данными
current_path = os.path.join('operations.json')


def main(path):
    """
    Файл принимает путь к json-файлу с банковскими операциями клиента. Далее происходит валидация
    содержимого файла и сортировка по дате по убыванию в случае корректности данных в файле.
    После происходит сокрытие номеров карт и счетов клиента с последующим выводом результата
    в формате:
    <Дата> <Описание>
    <От кого> -> <Кому>
    <Сумма> <Размерность>
    :param: str
    :return: str
    """
    sorted_data = operations_db(path)
    data_with_secreted_number = get_hide_number(sorted_data)
    result = get_transactions_result(data_with_secreted_number)
    return result


if __name__ == '__main__':
    print(main(current_path))
