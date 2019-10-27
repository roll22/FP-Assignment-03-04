import operator

from Setters_getters import get_apartment, get_type, set_amount, get_amount
from tools import create_expense


def add_expense(expenses, params):
    """
    Appends an expense to the given list
    :param expenses: The list of expenses
    :param params: params for creating an expense
    :return:
    """
    expense = create_expense(apartment=params[0],
                             type=params[1],
                             amount=params[2])
    expenses.append(expense)


def remove(expenses, params):
    """
    Removes expenses from the expenses list depending on the given parameters
    :param expenses: the list
    :param params: list of params
    :return:
    """
    if len(params) == 2:
        to_delete = []
        for idx, expense in enumerate(expenses):
            if params[0] <= get_apartment(expense) <= params[1]:
                to_delete.append(idx)
        for offset, index in enumerate(to_delete):
            index -= offset
            del expenses[index]
    if len(params) == 1:
        if type(params[0]) == int:
            to_delete = []
            for idx, expense in enumerate(expenses):
                if params[0] == get_apartment(expense):
                    to_delete.append(idx)
            for offset, index in enumerate(to_delete):
                index -= offset
                del expenses[index]
        else:
            to_delete = []
            for idx, expense in enumerate(expenses):
                if params[0] == get_type(expense):
                    to_delete.append(idx)
            for offset, index in enumerate(to_delete):
                index -= offset
                del expenses[index]


def replace(expenses, params):
    """
    Replaces expenses from the params
    :param expenses: the list of expenses
    :param params: list of params
    :return:
    """
    apartment = params[0]
    type = params[1]
    amount = params[2]
    for expense in expenses:
        if apartment == get_apartment(expense) and type == get_type(expense):
            set_amount(expense, amount)


def print_expense(expense):
    print('apartment: ' + str(get_apartment(expense)) +
          '  type: ' + get_type(expense) +
          '  amount: ' + str(get_amount(expense)))


def display(expenses, params):
    """
    Displays expenses
    :param expenses:
    :param params:
    :return:
    """
    if len(params) == 0:
        # 9 first 4 space 4 second 10 space 6 last

        for expense in expenses:
            print_expense(expense)

    elif len(params) == 1:
        for expense in expenses:
            if get_apartment(expense) == params[0]:
                print_expense(expense)

    elif len(params) == 2:
        sign = params[1]
        amount = params[0]

        def get_operator_fn(op):
            """
            Returns an operator from a string
            :param op: string
            :return: operator
            """
            return {
                '<': operator.lt,
                '<=': operator.le,
                '=': operator.eq,
                '>=': operator.ge,
                '>': operator.gt,
            }[op]

        sign = get_operator_fn(sign)
        for expense in expenses:
            if sign(get_amount(expense), amount):
                print_expense(expense)


def sum_of_expenses(expenses, params):
    """
    Prints the sum of the amount for the given type
    :param expenses:
    :param params:
    :return:
    """
    type = params[0]
    sum = 0
    for expense in expenses:
        if get_type(expense) == type:
            sum += get_amount(expense)
    print('sum of ' + type + ' is ' + str(sum))


def max_of_expenses(expenses, params):
    """
    Prints the maximum amount for the expenses having the given apartment
    :param expenses:
    :param params:
    :return:
    """
    apartment = params[0]
    types = ('water',
             'heating',
             'electricity',
             'gas',
             'other')
    for type in types:
        max_of_type = 0
        max_index = -1
        for expense in expenses:
            if get_amount(expense) > max_of_type and get_apartment(expense) == apartment and get_type(expense) == type:
                max_of_type = get_amount(expense)
                max_index = expenses.index(expense)
        if max_index != -1:
            print("max for " + type + ' for apartment ' + str(apartment) + ' is ' + str(max_of_type))
        else:
            print("No expense for type " + type + ' for apartment ' + str(apartment))


def compute_total_amount():
    pass


def sort_apartment(expenses):
    """

    :param expenses: the expenses list
    :return: a list of the apartments expenses
    """
    list_of_apartments = []
    for expense in expenses:
        if get_apartment(expense) not in list_of_apartments:
            list_of_apartments.append(get_apartment(expense))

    def sort_by_sublist(given_list):
        given_list.sort(key=lambda x: x[2])
        return given_list

    list_of_apartments = sort_by_sublist(list_of_apartments)
    return list_of_apartments


def sort_type(expenses):
    pass


def sort_expenses(expenses, params):
    """

    :param expenses:
    :param params:
    :return:
    """

    if params[0] == 'apartment':
        sort_apartment(expenses)

    elif params[0] == 'type':
        sort_type(expenses)


def filter(expenses, params):
    pass


def undo(expenses, params):
    pass