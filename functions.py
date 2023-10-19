import json
from datetime import datetime

def get_operations(path):
    """"
    Функция принимает путь к файлу .json с операциями
    Возвращает список словарей, представляющих операции 
    """
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def replace_datetime(operation):
    """
    Функция принимает словарь операции и заменяет дату строкой
    на дату объектом datetime для удобной последующей работы
    """
    operation['date'] = datetime.strptime(
        operation.get('date'),
        '%Y-%m-%dT%H:%M:%S.%f'  # "2018-01-26T15:40:13.413061"
        )
    return operation

def get_string_operation(operation):
    """
    Функция принимает операцию в виде словаря, возвращает строку в виде:
        14.10.2018 Перевод организации
        Visa Platinum 7000 79** **** 6361 -> Счет **9638
        82771.72 руб.
    """
    date = operation.get('date').strftime('%d.%m.%Y')  # Сразу в строке
    operation_amount = operation.get('operationAmount')
    amount = operation_amount.get('amount')
    valute = operation_amount.get('currency').get('name')
    description = operation.get('description')
    op_from = operation.get('from').split(' ')
    op_to = operation.get('to').split(' ')
    op_from_payment, op_from_number = ' '.join(op_from[:-1]), op_from[-1]
    op_from_number = (op_from_number[:4] + ' ' + op_from_number[4:6] 
                      + '** **** ' + op_from_number[-4:])
    op_to_payment, op_to_number = ' '.join(op_to[:-1]), op_to[-1]
    op_to_number = '**' + op_to_number[-4:]
    return (
        f'{date} {description}\n'
        f'{op_from_payment} {op_from_number} -> {op_to_payment} {op_to_number}\n'
        f'{amount} {valute}\n'
    )

def string_operations_generator(operations, count):
    """
    Функция-генератор принимает операции и количество операций для возврата
    Если операцию не получилось собрать соласно примеру, она не учитывается
    """
    i = 0
    for operation in operations:
        try:
            yield get_string_operation(operation)
            i += 1
        except Exception:
            continue
        if i > 4:
            return StopIteration