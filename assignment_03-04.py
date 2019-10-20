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
import re


def add_expense(expenses, params):
    expense = create_expense(apartment=params[0],
                             type=params[1],
                             amount=params[2])
    expenses.append(expense)


def remove(expenses, params):
    pass


def replace(expenses, params):
    pass


def display(expenses, params):
    pass


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

param 1  could be  
    -int (apartment)
    -string(type)
    -string (< > =)
    -int ( value) - filter
    -int (steps) - undo
    

'''


def read_command(usr_input):
    """
    Reads a command from the console and parses it returning a tuple

    :return:    cmd         :(str)   the function to call
                param1,     :(int)
                param2,     :(str)
                param3,     :(int)
                with_word   :(str)   'with'     if the command contains the word
                to_word     :(str)   'to'       if the command contains the word
    """
    # raw_input = input(">")
    raw_input = usr_input
    pattern = re.compile(r"""   \s*                                 
                                (?P<command>\b[a-zA-Z]*\b)\s* 
                                (?P<param1>\b\d*\b)\s*
                                (?P<with>\bwith\b)?\s*
                                (?P<to>\bto\b)?\s*
                                (?P<param2>\b[a-zA-Z]*\b)\s*
                                (?P<param3>\b\d*\b)\s*
                                
                                """, re.VERBOSE)
    match = pattern.match(raw_input)
    cmd = None
    param1 = None
    param2 = None
    param3 = None
    with_word = None
    to_word = None
    if match is not None:
        cmd = match.group("command")
        param1 = match.group("param1")
        param2 = match.group("param2")
        param3 = match.group("param3")
        with_word = match.group("with")
        to_word = match.group("to")

    return cmd, [param1, param2, param3, with_word, to_word]


def validate_add_params(params):
    """
    Validates the needed params
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
        if apartment <= 0:
            raise ValueError('apartment')

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
    pass


def validate_replace_params(params):
    pass


def validate_display_params(params):
    pass


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


def main():
    pass


def test_read_command():
    user_inputs = ['     add 2 gas 200',
                   'add 01 electricity 200']
                    # 'remove 15',
    # 'remove 5 to 10',
    # 'remove gas',
    # 'replace 12 gas with 200',
    # 'list',
    # 'list 15',
    # 'list > 100',
    # 'list = 17',
    # 'sum gas',
    # 'max 25',
    # 'sort apartment',
    # 'sort type',
    # 'filter gas',
    # 'filter 300',
    # 'undo 12']
    expenses = []
    for user_input in user_inputs:

        cmd, params = read_command(user_input)
        cmds = {'add': [add_expense, validate_add_params],
                'remove': [remove, validate_remove_params],
                'replace': replace,
                'list': display,
                'sum': sum_of_expenses,
                'max': max_of_expenses,
                'sort': sort_expenses,
                'filter': filter,
                'undo': undo}

        function_to_call = validate_command(commands=cmds, cmd=cmd)
        if function_to_call is not None:
            validation_function_to_run = cmds[cmd][1]
            try:
                params = validation_function_to_run(params)
            except ValueError as exception:
                print('Failed: Bad ' + str(exception.args[0]))
                params = None

            if params is not None:
                function_to_call(expenses, validation_function_to_run(params))
            print(expenses)
        elif cmd == 'exit':
            return
        else:
            print("bad command")


test_read_command()
'''
add 12 food 
'''
