from validations import validate_positive_int_range, validate_not_empty

def add_student(students):
    id = len(students) +1
    name = validate_not_empty("Enter the name of the student: ")
    program = validate_not_empty("Enter the program of the student: ")
    status = validate_positive_int_range('Enter "1" for active or "2" for inactive: ', 2)
    if status == 1:
        status = "Active"
    else:
        status = "Inactive"

    new_student = {
        "id" : id,
        "name" : name,
        "program" : program,
        "status" : status
    }
    students.append(new_student)
    return students
