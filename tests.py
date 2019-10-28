from Functionalities import add_expense, remove, replace, display, sum_of_expenses, max_of_expenses, sort_expenses, \
    filter_expense, undo
from tools import init_expenses, read_command
from validations import validate_add_params, validate_remove_params, validate_replace_params, validate_display_params, \
    validate_sum_of_expenses_params, validate_max_of_expenses_params, validate_sort_expenses_params, \
    validate_filter_params, validate_undo_params, validate_command


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
                   'list < 130',
                   'sum gas',
                   'max 25',
                   'sort apartment',
                   'sort type',
                   'filter gas',
                   'filter 300',
                   'undo 12']

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
                'filter': [filter_expense, validate_filter_params],
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
