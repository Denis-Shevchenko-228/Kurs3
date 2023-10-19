import json
from datetime import datetime

from functions import (
    get_operations,
    get_string_operation,
    string_operations_generator,
    replace_datetime,
)

TEST_OPERATION_JSON = """
{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
}
"""
TEST_OPERATION_DICT = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": datetime(2019, 8, 26, 10, 50, 58, 294041),
    "operationAmount": {
        "amount": "31957.58",
        "currency": {"name": "руб.", "code": "RUB"},
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}
TEST_OPERATION_STRING = (
    "26.08.2019 Перевод организации\n"
    "Maestro 1596 83** **** 5199 -> Счет **9589\n"
    "31957.58 руб.\n"
)


def test_get_operations_data():
    assert get_operations("operations.json") != []
    try:
        get_operations("some_null_name.json")
    except Exception as e:
        assert str(e) == "[Errno 2] No such file or directory: 'some_null_name.json'"


def test_replace_datetime():
    print(json.loads(TEST_OPERATION_JSON))
    assert replace_datetime(json.loads(TEST_OPERATION_JSON)) == TEST_OPERATION_DICT


def test_get_string_operation():
    assert get_string_operation(TEST_OPERATION_DICT) == TEST_OPERATION_STRING


def test_string_operations_generator():
    assert (
        list(
            string_operations_generator(
                [dict(value=1), dict(value2=2), TEST_OPERATION_DICT] * 10, 5
            )
        )
        == [TEST_OPERATION_STRING] * 5
    )
