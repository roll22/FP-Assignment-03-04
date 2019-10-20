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


def add_transaction():
    pass


def remove():
    pass


def replace():
    pass


def display_w_properties():
    pass


def filter():
    pass


def undo():
    pass


def create_expense(apartment, amount, type):
    return [apartment, amount, type]

'''
cmd int tip int
add <apartment> <type> <amount>
remove <apartment>
remove <start apartment> to <end apartment>
remove <type>
replace <apartment> <type> with <amount>
list
list <apartment>
list [ < | = | > ] <amount>
sum <type>
max <apartment>
sort apartment
sort type
filter <type>
filter <value>
undo <steps>

'''

def read_command():
    """
    Reads a command from the console and parses it
    :return:
    """
    raw_input = input(">")
    pattern = re.compile(r"""   \s*                                 
                                (?P<command>\b[a-zA-Z]*\b)\s* 
                                (?P<param1>\b\d*\b)\s*
                                (?P<param2>\b[a-zA-Z]*\b)\s*
                                (?P<param3>\b\d*\b)\s*
                                """, re.VERBOSE)
    match = pattern.match(raw_input)
    cmd = None
    param1 = None
    param2 = None
    param3 = None
    if match is not None:
        cmd = match.group("command")
        param1 = match.group("param1")
        param2 = match.group("param2")
        param3 = match.group("param3")
    return cmd, param1, param2, param3


def validate_command(cmd, param1, param2, param3):
    pass


def main():
    pass


read_command()

'''
add 12 food 
'''
