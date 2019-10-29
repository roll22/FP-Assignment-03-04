import re


def create_expense(apartment, type, amount):
    """
    Creates the list with ap. on pos 0, amount on 1, and type on 2
    :param apartment:
    :param type:
    :param amount:
    :return: expense as a list
    """
    return [apartment, type, amount]


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
    # Debugging
    if usr_input is None:
        raw_input = input(">")
    else:
        raw_input = usr_input

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


def init_expenses():
    expenses = [[1, 'electricity', 200],
                [2, 'gas', 200],
                [2, 'electricity', 13],
                [3, 'water', 12],
                [4, 'heating', 2],
                [5, 'gas', 200],
                [6, 'electricity', 40],
                [7, 'gas', 123],
                [8, 'other', 13],
                [9, 'other', 15],
                [10, 'other', 155]]
    return expenses


def check_list_identicity(expenses, hist_expenses):
    test = True
    for idx in range(0, len(expenses)):
        for idx2 in range(0, len(expenses[idx])):
            try:
                if expenses[idx][idx2] != hist_expenses[idx][idx2]:
                    test = False
            except Exception:
                test = False
    return test
