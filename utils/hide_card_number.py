def get_hide_number(lst):
    """
    Функция принимает список с отсортированными по дате банковскими операциями клиента и
    возвращает список со скрытыми номерами карт и счетов клиента. Подразумевается, что вначале будет вызов
    функции operations_db для валидации входных данных. В случае ее отсутствия и некорректности данных
    будет возбуждено исключение с оповещением о необходимости валидации данных.
    :param lst: list
    :return: list
    """
    for elem in lst:
        try:
            if elem.get('from'):
                elem["from"] = elem["from"].split()
                title_from = ' '.join(elem["from"][:len(elem["from"]) - 1])
                number_from = elem["from"][-1]
                if len(number_from) <= 16:
                    number_from = f'{number_from:.4} {number_from[4:6]}** **** {number_from[-4:]}'
                else:
                    number_from = f'**{number_from[-4:]}'
                elem["from"] = title_from + ' ' + number_from

            elem["to"] = elem["to"].split()
            title_to = ' '.join(elem["to"][:len(elem["to"]) - 1])
            number_to = elem["to"][-1]
            if len(number_to) <= 16:
                title_to = f'{number_to:.4} {number_to[4:6]}** **** {number_to[-4:]}'
            else:
                number_to = f'**{number_to[-4:]}'
            elem["to"] = title_to + ' ' + number_to
        except (KeyError, TypeError, AttributeError):
            return f'Проверьте данные в файле. ' \
                   f'Подразумевается вызов функции operations_db перед исполнением get_hide_number'
    return lst
