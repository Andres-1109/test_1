def validate_positive_int_range(message, max_range=None):
    while True:
        try:
            number = int(input(message))
            if 1> number > max_range:
                if max_range == None:
                    print("Invalid answer")
                else:
                    print(f'Invalid answer. Enter a number between 0 and {max_range}')
            else:
                return number
        except ValueError:
            if max_range == None:
                print("Invalid answer")
            else:
                print(f'Invalid answer. Enter a number between 0 and {max_range}')

def validate_not_empty(message):
    while True:
        try:
            answer = input(message)
            if answer != "":
                return answer
            else:
                print("Please write something")
        except ValueError:
            print("Please write something")