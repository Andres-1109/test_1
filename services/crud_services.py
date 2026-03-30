from validations import validate_positive_int_range, validate_not_empty

def add_student(students, id):
    id+= 1
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
    return students, id

def delete_student(students, id):
    if students == []:
        print("There are no students to delete")
    else:
        number_of_students = len(students)
        for i, student in enumerate(students, start= 1):
            print(f'{i} . |ID: {student["id"]}| Name: {student["name"]}| Program: {student["program"]}| Status: {student["status"]}|')
        choice = validate_positive_int_range("Enter the number of the student to delete: ", number_of_students) -1
        students.pop(choice)
    return students, id    

def edit_student(students, id):
    if students == []:
        print("There are no students to edit")
    else:
        number_of_students = len(students)
        for i, student in enumerate(students, start= 1):
            print(f'{i} . |ID: {student["id"]}| Name: {student["name"]}| Program: {student["program"]}| Status: {student["status"]}|')
        choice = validate_positive_int_range("Enter the number of the student to delete: ", number_of_students) -1
        
        students[choice]["name"] = validate_not_empty("Enter the name of the student: ")
        students[choice]["program"] = validate_not_empty("Enter the program of the student: ")
        students[choice]["status"] = validate_positive_int_range('Enter "1" for active or "2" for inactive: ', 2)
    return students, id

def show_students(students, id):
    if students == []:
        print("There are no students to show")
    else:
        for i, student in enumerate(students, start= 1):
            print(f'{i} . |ID: {student["id"]}| Name: {student["name"]}| Program: {student["program"]}| Status: {student["status"]}|')
    return students, id