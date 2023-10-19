
from settings import (
    TRANSACTIONS_PATH as TP,
    COUNT_LAST_OPERATIONS as CO
    )

from functions import (
    get_operations,
    replace_datetime,
    string_operations_generator
    )


def main():
    transactions = get_operations(TP)
    executed_transactions = filter(
        lambda x: x.get('state') == 'EXECUTED', 
        transactions
        )
    transactions_with_datetime = map(
        replace_datetime,
        executed_transactions
        )
    sorted_transactions = sorted(
        transactions_with_datetime, 
        key=lambda x: x.get('date'),
        reverse=True
        )
    for operation in string_operations_generator(
            sorted_transactions,
            CO
        ):
        print(operation)


if __name__ == '__main__':
    main()