from Functionalities import \
    add_expense, \
    remove, \
    replace, \
    display, \
    sum_of_expenses, \
    max_of_expenses, \
    sort_expenses, \
    filter_expense, \
    undo
from tools import read_command, init_expenses, check_list_identicity
from validations import validate_add_params, validate_remove_params, validate_replace_params, validate_display_params, \
    validate_sum_of_expenses_params, validate_max_of_expenses_params, validate_sort_expenses_params, \
    validate_filter_params, validate_undo_params, validate_command
import re
import operator
import copy


def add_menu(expenses):
    types = ('water',
             'heating',
             'electricity',
             'gas',
             'other')
    aparts = input("input apartment >")
    if aparts.isdigit():
        aparts = int(aparts)
        type = input("input type >")
        if type in types:
            amount = input('input amouunt! >')
            if amount.isdigit():
                amount = int(amount)
                add_expense(expenses, [aparts, type, amount])
    else:
        raise ValueError('params!')


def remove_menu(expenses):
    types = ('water',
             'heating',
             'electricity',
             'gas',
             'other')

    print('1.remove by apartment\n'
          '2.remove apartment to apartment\n'
          '3.remove type')
    choice = input('>')
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            aparts = input('input apartments!')
            if aparts.isdigit():
                aparts = int(aparts)
                remove(expenses, [aparts])
            else:
                raise ValueError('apartment!')
        elif choice == 2:
            ap1 = input('input first apartment!')
            ap2 = input('input second apartment!')
            if ap1.isdigit() and ap2.isdigit():
                remove(expenses, [ap1, ap2])
            else:
                raise ValueError('apartments!')
        elif choice == 3:
            type = input('input type!')
            if type in types:
                remove(expenses, [type])
            else:
                raise ValueError('type!')
    else:
        raise ValueError('choice!')


def replace_menu(expenses):
    types = ('water',
             'heating',
             'electricity',
             'gas',
             'other')
    aparts = input("input apartment >")
    if aparts.isdigit():
        aparts = int(aparts)
        type = input("input type >")
        if type in types:
            amount = input()
            if amount.isdigit():
                amount = int(amount)
                replace(expenses, [aparts, type, amount])
    else:
        raise ValueError('params!')


def list_menu(expenses):
    types = ('water',
             'heating',
             'electricity',
             'gas',
             'other')

    print('1.list\n'
          '2.list apartment\n'
          '3.list <sign> amount\n')
    choice = input('>')
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            display(expenses, [])
        elif choice == 2:
            ap1 = input('input apartment!')
            if ap1.isdigit():
                display(expenses, [ap1])
            else:
                raise ValueError('apartments!')
        elif choice == 3:
            sign = input('input sign(< > =)!')
            amount = input('input amount!')
            if amount.isdigit():
                amount = int(amount)
            else:
                raise ValueError('amount!')
            if sign in ('>', '<', '='):
                pass
            else:
                raise ValueError('sign!')
            display(expenses, [amount, sign])


def sum_menu(expenses):
    types = ('water',
             'heating',
             'electricity',
             'gas',
             'other')

    type = input('input type')
    if type in types:
        sum_of_expenses(expenses, [type])


def max_menu(expenses):
    apart = input('input apartment!')
    if apart.isdigit():
        apart = int(apart)
        max_of_expenses(expenses, [apart])
    else:
        raise ValueError('apartment!')


def sort_menu(expenses):
    types = ('water',
             'heating',
             'electricity',
             'gas',
             'other')

    print('1.sort by apartment\n'
          '2.sort by type')
    choice = input('>')
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            sort_expenses(expenses, ['apartment'])
        elif choice == 2:
            sort_expenses(expenses, ['type'])
    else:
        raise ValueError('choice!')


def filter_menu(expenses):
    types = ('water',
             'heating',
             'electricity',
             'gas',
             'other')
    print('1.filter by amount\n'
          '2.filter by type\n')
    choice = input('>')
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            amount = input('input amount!')
            if amount.isdigit():
                amount = int(amount)
                filter_expense(expenses, [amount])
            else:
                raise ValueError('amount!')
        elif choice == 2:
            type = input('input type!')
            if type in types:
                filter_expense(expenses, [type])
            else:
                raise ValueError('type!')
    else:
        raise ValueError('choice!')

def print_menu():
    print('1.add\n'
          '2.remove\n'
          '3.replace\n'
          '4.list\n'
          '5.sum\n'
          '6.max\n'
          '7.sort\n'
          '8.filter\n'
          '9.undo\n'
          '0.exit')


def read_command_menu():
    expenses = init_expenses()
    history_expenses = []
    history_expenses.append(copy.deepcopy(expenses))
    while True:
        print_menu()
        expenses = copy.deepcopy(history_expenses[len(history_expenses)-1])
        raw_input = input(">")
        pattern = re.compile(r"""\s*(?P<input>\b[0-9]\b)\s*""")
        match = pattern.match(raw_input)
        choice = None
        if match is not None:
            choice = match.group("input")
            choices = {
                '1': add_menu,
                '2': remove_menu,
                '3': replace_menu,
                '4': list_menu,
                '5': sum_menu,
                '6': max_menu,
                '7': sort_menu,
                '8': filter_menu,
                '9': undo,
            }
            try:
                if choice == '9':
                    choices[choice](expenses, history_expenses)
                else:
                    choices[choice](expenses)

            except KeyError:
                pass
            except ValueError as error:
                print('Bad ' + str(error.args[0]))
            if choice != '9' and not check_list_identicity(expenses, history_expenses[len(history_expenses) - 1]):
                # print('appended')
                history_expenses.append(copy.deepcopy(expenses))
            print(' ')
            if choice == '0':
                return
        else:
            print("Bad Command!")


def menu_main_functionality():
    read_command_menu()

