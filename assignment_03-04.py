'''
Jane is the administrator of an apartment building and she wants
to manage the monthly expenses for each apartment.

Jane needs an application to
store,
 for a given month,
 the expenses for each apartment.
Each expense is stored in the application using the 
following elements:
    apartment (number of apartment,positive integer),
    amount (positive integer),
    type (from one of the predefined categories: water, heating,
            electricity, gas, other).

1. Add a new transaction to the list.
add <apartment> <type> <amount>
e.g.
add 25 gas 100 – add to apartment 25 an expense for gas 
in amount of 100 RON.

2. Modify expenses from the list.
remove <apartment>
remove <start apartment> to <end apartment>
remove <type>
replace <apartment> <type> with <amount>
e.g.
remove 15 – remove all the expenses of apartment 15.
remove 5 to 10 – remove all the expenses from apartments between 5 and 10.
remove gas – remove all the expenses for gas from all apartments.
replace 12 gas with 200 – replace the amount of the expense 
with type gas for apartment 12 with 200 RON.

3. Write the expenses having different properties.
list
list <apartment>
list [ < | = | > ] <amount>
e.g.
list – write the entire list of expenses.
list 15 – write all expenses for apartment 15.
list > 100 - write all the apartments having total expenses > 100 RON.
list = 17 - write all the apartments having total expenses = 17 RON.

4. Obtain different characteristics of the expenses.
sum <type>
max <apartment>
sort apartment
sort type
e.g.
sum gas – write the total amount for the expenses having type “gas”.
max 25 – write the maximum amount per each expense type for apartment 25.
sort apartment – write the list of apartments sorted
 ascending by total amount of expenses.
sort type – write the total amount of expenses for each type,
 sorted ascending by amount ofmoney.

5. Filter.
filter <type>
filter <value>
e.g.
filter gas – keep only expenses for “gas”.
filter 300 – keep only expenses having an amount of money smaller
 than 300 RON.

6. Undo the last operation that modified program data.
undo – the last operation that has modified program data will
 be reversed. The user has to be able
to undo all operations performed since program start by
 repeatedly calling this function.
undo <steps>

COMMANDS
MENU
REGEX

'''
import operator
import re


def get_apartment(expense):
    return expense[0]


def get_type(expense):
    return expense[1]


def get_amount(expense):
    return expense[2]


def set_amount(expense, amount):
    expense[2] = amount


def add_expense(expenses, params):
    expense = create_expense(apartment=params[0],
                             type=params[1],
                             amount=params[2])
    expenses.append(expense)


def remove(expenses, params):
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

    :param expenses:
    :param params:
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
    pass


def max_of_expenses(expenses, params):
    pass


def sort_expenses(expenses, params):
    pass


def filter(expenses, params):
    pass


def undo(expenses, params):
    pass


def create_expense(apartment, type, amount):
    """
    Creates the list with ap. on pos 0, amount on 1, and type on 2
    :param apartment:
    :param type:
    :param amount:
    :return: expense as a list
    """
    return [apartment, type, amount]


'''
cmd int tip int
add int <apartment> str<type> int<amount>
remove int<apartment>
remove int<start apartment> to int<end apartment>
remove str<type>
replace int<apartment> str<type> with int<amount>
list
list int<apartment>
list str[ < | = | > ] int<amount>
sum str<type>
max int<apartment>
sort int<apartment
sort str<type
filter str<type>
filter int<value>
undo int<steps>
'''


def read_command(usr_input=None):
    """
    Reads a command from the console and parses it returning a tuple

    :return:    cmd         :(str)   the function to call
                param1,     :(int)
                param2,     :(str)
                param3,     :(int)
                with_word   :(str)   'with'     if the command contains the word
                to_word     :(str)   'to'       if the command contains the word
    """
    raw_input = input(">")
    #raw_input = usr_input
    pattern = re.compile(r"""   \s*                                 
                                (?P<command>\b[a-zA-Z]*\b)\s* 
                                (?P<sign>[<>=]{1,2})?\s*
                                (?P<param1>\b\d*\b)\s*
                                (?P<with>\bwith\b)?\s*
                                (?P<to>\bto\b)?\s*
                                (?P<param2>\b[a-zA-Z]*\b)\s*
                                (?P<with_optional>\bwith\b)?\s*
                                (?P<param3>\b\d*\b)\s*
                                
                                """, re.VERBOSE)
    match = pattern.match(raw_input)
    cmd = None
    param1 = None
    param2 = None
    param3 = None
    with_word = None
    to_word = None
    sign = None
    if match is not None:
        cmd = match.group("command")
        param1 = match.group("param1")
        param2 = match.group("param2")
        param3 = match.group("param3")
        with_word = match.group("with")
        sign = match.group("sign")
        if match.group("with_optional") is not None:
            with_word = match.group("with_optional")
        if sign is not None and param2 is '':
            param2 = sign
        to_word = match.group("to")

    return cmd, [param1, param2, param3, with_word, to_word]


def validate_add_params(params):
    """
    Validates the needed params for add function
    Raises ValueError for invalid parameters
    :param params: list of params
    :return:list of useful params
    """
    # no need to try/except int() because of regex parsing
    apartment = params[0]
    if apartment == '':
        raise ValueError('apartment')
    else:
        apartment = int(apartment)
    types = ('water',
             'heating',
             'electricity',
             'gas',
             'other')
    type = params[1]
    if type not in types:
        raise ValueError('type')

    amount = params[2]
    if amount == '':
        raise ValueError('amount')
    else:
        amount = int(amount)

    return apartment, type, amount


def validate_remove_params(params):
    """
    Validates the needed params for remove function
    Raises ValueError for invalid parameters
    :param params: list of params
    :return:list of useful params
    """
    if params[0] is not '' and params[4] == 'to' and params[2] is not '':
        start_apart = int(params[0])
        end_apart = int(params[2])
        if start_apart > end_apart:
            return end_apart, start_apart
        else:
            return start_apart, end_apart
    elif params[0] is not '' and params[1] is '' and params[2] is '' and params[3] is None and params[4] is None:
        apartment1 = int(params[0])
        returnable = [apartment1]
        return tuple(returnable)
    elif params[0] is '' and params[1] is not '' and params[2] is '' and params[3] is None and params[4] is None:
        type = params[1]
        returnable = [type]
        return tuple(returnable)
    else:
        raise ValueError('parameters!')


def validate_replace_params(params):
    """
    Validates the needed params
    Raises ValueError for invalid parameters
    :param params: list of params
    :return:list of useful params
    replace int<apartment> str<type> with int<amount>
    """
    apartment = params[0]
    if apartment == '':
        raise ValueError('apartment')
    else:
        apartment = int(apartment)

    types = ('water',
             'heating',
             'electricity',
             'gas',
             'other')
    type = params[1]
    if type not in types:
        raise ValueError('type')

    amount = params[2]
    print('amount = ' + str(amount))
    if amount == '':
        raise ValueError('amount')
    else:
        amount = int(amount)

    return apartment, type, amount


def validate_display_params(params):
    '''
                    'list',
    #               'list 15',
    #               'list > 100',
    #               'list = 17',
    #               'list < 130,
    :param params:
    :return:
    '''

    if params[0] is not '' and params[1] in ['<', '>', '=', '>=', '<=']:
        amount = int(params[0])
        sign = params[1]
        return amount, sign
    elif params[0] is not '' and params[1] is '' and params[2] is '' and params[3] is None and params[4] is None:
        apartment = int(params[0])
        returnable = [apartment]
        return tuple(returnable)
    elif params[0] is '' and params[1] is '' and params[2] is '' and params[3] is None and params[4] is None:
        return ()
    else:
        raise ValueError('parameters!')


def validate_sum_of_expenses_params(params):
    pass


def validate_max_of_expenses_params(params):
    pass


def validate_sort_expenses_params(params):
    pass


def validate_filter_params(params):
    pass


def validate_undo_params(params):
    pass


def validate_command(commands, cmd):
    try:
        return commands[cmd][0]
    except KeyError:
        return None


def init_expenses():
    expenses = [[1, 'electricity', 200],
                [2, 'gas', 200],
                [2, 'electricity', 13],
                [3, 'water', 200],
                [4, 'heating', 200],
                [5, 'gas', 200],
                [6, 'electricity', 200],
                [7, 'gas', 200],
                [8, 'other', 200],
                [9, 'other', 200],
                [10, 'other', 200]]
    return expenses


def main():
    expenses = init_expenses()
    # for user_input in user_inputs:
    while True:
        cmd, params = read_command()
        cmds = {'add': [add_expense, validate_add_params],
                'remove': [remove, validate_remove_params],
                'replace': [replace, validate_replace_params],
                'list': [display, validate_display_params],
                'sum': [sum_of_expenses, validate_sum_of_expenses_params],
                'max': [max_of_expenses, validate_max_of_expenses_params],
                'sort': [sort_expenses, validate_sort_expenses_params],
                'filter': [filter, validate_filter_params],
                'undo': [undo, validate_undo_params]}

        # checks if the command exists and returns the function
        function_to_call = validate_command(commands=cmds, cmd=cmd)
        if function_to_call is not None:
            # gets validation function
            validation_function_to_run = cmds[cmd][1]
            # validation
            try:
                # print('cmd = ', cmd)
                # print('params = ', params)
                params = validation_function_to_run(params)
            except ValueError as exception:
                print('Failed: Bad ' + str(exception.args[0]))
                params = None

            # calls function with proper params
            if params is not None:
                function_to_call(expenses, params)
            # for expense in expenses:
            #     print(expense)
            print(' ')
        elif cmd == 'exit':
            return
        else:
            print("bad command\n")


def test_read_command():
    user_inputs = ['     add 2 gas 200',
                   'exitasf gdsjkohn',
                   'add 01 electricity 200',
                   'remove 2',
                   'remove 5 to 6',
                   'remove gas',
                   'replace 10 other with 0 ',
                   'list',
                   'list 15',
                   'list >= 100',
                   'list = 200',
                   'list < 130', ]
    # 'sum gas',
    # 'max 25',
    # 'sort apartment',
    # 'sort type',
    # 'filter gas',
    # 'filter 300',
    # 'undo 12']
    expenses = init_expenses()
    for user_input in user_inputs:

        cmd, params = read_command(user_input)
        cmds = {'add': [add_expense, validate_add_params],
                'remove': [remove, validate_remove_params],
                'replace': [replace, validate_replace_params],
                'list': [display, validate_display_params],
                'sum': [sum_of_expenses, validate_sum_of_expenses_params],
                'max': [max_of_expenses, validate_max_of_expenses_params],
                'sort': [sort_expenses, validate_sort_expenses_params],
                'filter': [filter, validate_filter_params],
                'undo': [undo, validate_undo_params]}

        # checks if the command exists and returns the function
        function_to_call = validate_command(commands=cmds, cmd=cmd)
        if function_to_call is not None:
            # gets validation function
            validation_function_to_run = cmds[cmd][1]
            # validation
            try:
                print('cmd = ', cmd)
                print('params = ', params)
                params = validation_function_to_run(params)
            except ValueError as exception:
                print('Failed: Bad ' + str(exception.args[0]))
                params = None

            # calls function with proper params
            if params is not None:
                function_to_call(expenses, params)
            for expense in expenses:
                print(expense)
            print(' ')
        elif cmd == 'exit':
            return
        else:
            print("bad command\n")


#test_read_command()
main()