from data.menu_options import menu_options
from validations import validate_positive_int_range


def initial_menu(students):
    while True:
        options = menu_options()
        number_of_options = len(options)
        
        for i, option in enumerate(options, start=1):
            print(f'{i}. {option["option"]}')

        choice = validate_positive_int_range("Choose an option: ", number_of_options) -1

        students = options[choice]["action"](students)
        print(students)
        if students == "exit":
            break