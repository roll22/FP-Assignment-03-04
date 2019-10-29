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
import copy

def command_main_functionality():
    expenses = init_expenses()
    history_expenses = []
    copy_of_list = copy.deepcopy(expenses)
    history_expenses.append(copy_of_list)
    while True:
        expenses = copy.deepcopy(history_expenses[len(history_expenses) - 1])
        cmd, params = read_command()
        cmds = {'add': [add_expense, validate_add_params],
                'remove': [remove, validate_remove_params],
                'replace': [replace, validate_replace_params],
                'list': [display, validate_display_params],
                'sum': [sum_of_expenses, validate_sum_of_expenses_params],
                'max': [max_of_expenses, validate_max_of_expenses_params],
                'sort': [sort_expenses, validate_sort_expenses_params],
                'filter': [filter_expense, validate_filter_params],
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
                function_to_call = None
            # we provide the history list as params for the undo function
            if function_to_call == undo:
                params = history_expenses
            # calls function with proper params
            if params is not None:
                function_to_call(expenses, params)
            print(' ')
            # we check if we modified the expense and if so we add an entry in history
            if function_to_call != undo and not check_list_identicity(expenses, history_expenses[len(history_expenses)-1]):
                print('appended')
                history_expenses.append(copy.deepcopy(expenses))
        elif cmd == 'exit':
            return
        else:
            print("bad command\n")
