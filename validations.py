def validate_positive_int_range(message, max_range=None):
    while True:
        try:
            number = int(input(message))
            if max_range != None:
                if number > max_range or number < 1:
                    print(f'Invalid answer. Enter a number between 0 and {max_range}')
                else:
                    return number
            else:
                if number < 1:
                    print("Invalid answer")
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

def validate_id_csv(students, id):
    for student in students:
        if student["id"] == id:
            return ValueError
    return id
    
def validate_name_csv(name):
    if name != "":
        return name
    else:
        return ValueError
    
def validate_status_csv(status):
    if status == "Active" or status == "Inactive":
        return status
    else:
        return ValueError

