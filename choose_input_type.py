import re
from command_ui import command_main_functionality
from menu_ui import menu_main_functionality


def choose_input():
    while True:
        raw_input = input("1.Command Based Input\n"
                          "2.Menu Based Input\n"
                          "3.Exit\n"
                          ">")
        pattern = re.compile(r"""\s*(?P<input>\b[1-3]\b)\s*""")
        match = pattern.match(raw_input)
        choice = None
        if match is not None:
            choice = match.group("input")
            if choice is '1':
                command_main_functionality()
                break
            elif choice is '2':
                menu_main_functionality()
                break
            elif choice is '3':
                print("User Cancelled!")
                break
        else:
            print("Bad Command!")
