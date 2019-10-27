from Functionalities import \
    add_expense, \
    remove, \
    replace, \
    display, \
    sum_of_expenses, \
    max_of_expenses, \
    sort_expenses, \
    filter, \
    undo
from tools import read_command, init_expenses
from validations import validate_add_params, validate_remove_params, validate_replace_params, validate_display_params, \
    validate_sum_of_expenses_params, validate_max_of_expenses_params, validate_sort_expenses_params, \
    validate_filter_params, validate_undo_params, validate_command

'''
add int<apartment> str<type> int<amount>
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
'''
program start
main
choose_menu
    command
        command_main()

    menu
        menu_main()


'''


def print_menu():
    print('1.add')


def main_functionality(expenses, history_expenses):
    expenses = init_expenses()
    history_expenses = [expenses]
    no_of_commands = 0
    while True:
        print_menu()
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

            print(' ')
        elif cmd == 'exit':
            return
        else:
            print("bad command\n")
