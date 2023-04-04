from utils.db_operations import operations_db
import os.path

# Объявление текущего пути к файлу с данными
current_path = os.path.join('../utils', 'operations.json')


def main(path):
    """
    Функция возвращает строку в формате:
    <Дата> <Описание>
    <От кого> -> <Кому>
    <Сумма> <Размерность>
    Если в файле отсутствует <От кого>, то функция возвращает — <Кому>.
    :param path: str
    :return: str
    """
    # Вызов функции operations_db с отсортированным списком с данными о транзакциях
    transactions = operations_db(path)
    res = ""
    for elem in transactions:
        # К результату инкриминирует <Дата> <Описание>
        res += f'{elem["date"]} {elem["description"]}\n'

        # Проверка наличия отправителя
        if elem.get('from'):
            elem["from"] = elem["from"].split()
            title_from = ' '.join(elem["from"][:len(elem["from"]) - 1])
            number_from = elem["from"][-1]
            if len(number_from) <= 16:
                number_from = f'{number_from:.4} {number_from[4:6]}** **** {number_from[-4:]}'
            else:
                number_from = f'**{number_from[-4:]}'
            # Инкриминирует <От кого> к результирующей строке
            res += f'{title_from} {number_from} -> '

        elem["to"] = elem["to"].split()
        title_to = ' '.join(elem["to"][:len(elem["to"]) - 1])
        number_to = elem["to"][-1]
        if len(number_to) <= 16:
            title_to = f'{number_to:.4} {number_to[4:6]}** **** {number_to[-4:]}'
        else:
            number_to = f'**{number_to[-4:]}'
        # Инкриминирует <Кому> к результирующей строке
        res += f'{title_to} {number_to}\n'
        # Инкриминирует <Сумма> <Размерность> к результирующей строке
        res += f'{elem["operationAmount"]["amount"]} {elem["operationAmount"]["currency"]["name"]}\n\n'
    return res


print(main(current_path))
