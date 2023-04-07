def get_transactions_result(lst):
    """
    Функция принимает список с отсортированными по дате банковскими операциями клиента.
    Подразумевается, что вначале будет вызов функции operations_db и get_hide_number для
    валидации входных данных и сокрытия номеров карт и счетов клиента. В случае некорректности
    данных будет возбуждено исключение с оповещением о необходимости валидации данных.
    Функция возврает строку в формате:
    <Дата> <Описание>
    <От кого> -> <Кому>
    <Сумма> <Размерность>
    Если в файле отсутствует <От кого>, то функция возвращает — <Кому>.
    :param lst:
    :return: str
    """
    res = ''
    for elem in lst:
        try:
            res += f'{elem["date"]} {elem["description"]}\n'
            if elem.get("from"):
                res += f'{elem["from"]} -> '
            res += f'{elem["to"]}\n'
            res += f'{elem["operationAmount"]["amount"]} {elem["operationAmount"]["currency"]["name"]}\n\n'
        except (KeyError, TypeError, AttributeError):
            return f'Проверьте данные в файле. ' \
                   f'Подразумевается вызов функции operations_db и get_hide_number ' \
                   f'перед исполнением get_transactions_result'
    return res
