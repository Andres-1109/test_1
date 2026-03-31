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

def search_students(students,id):
    if students == []:
        print("There are no students to search")
        return students, id
    else:
        choice= validate_positive_int_range('''
Press                                        
"1" to search by ID
"2" to search by Name
"3" to search by Program
"4" to search by Status                                            
Your choice: ''', 4)
        counter = 0  # Counter to validate if there was an student found and if not print a message that says 'Student not found'
        if choice == 1:
            data_to_search = validate_positive_int_range("Enter the ID to search: ")
            for i, student in enumerate(students, start=1):
                if student["id"] == data_to_search:
                    print(f'{i} . |ID: {student["id"]}| Name: {student["name"]}| Program: {student["program"]}| Status: {student["status"]}|')
                    counter+=1
            if counter == 0:
                print("ID not found")
            return students, id
        elif choice == 2:
            data_to_search = validate_not_empty("Enter the name to search: ").lower()
            for i, student in enumerate(students, start=1):
                if student["name"].lower() == data_to_search:
                    print(f'{i} . |ID: {student["id"]}| Name: {student["name"]}| Program: {student["program"]}| Status: {student["status"]}|')
                    counter+=1
            if counter == 0:
                print("Name not found")
            return students, id
        elif choice ==3:
            data_to_search = validate_not_empty("Enter the program to search: ").lower()
            for i, student in enumerate(students, start=1):
                if student["program"].lower() == data_to_search:
                    print(f'{i} . |ID: {student["id"]}| Name: {student["name"]}| Program: {student["program"]}| Status: {student["status"]}|')
                    counter+=1
            if counter == 0:
                print("Program not found")
            return students, id
        else:
            data_to_search = validate_positive_int_range('Enter "1" to search active students or "2" for inactive students: ', 2)
            if data_to_search == 1:
                data_to_search = "Active"
            else:
                data_to_search = "Incactive"
            for i, student in enumerate(students, start=1):
                if student["status"] == data_to_search:
                    print(f'{i} . |ID: {student["id"]}| Name: {student["name"]}| Program: {student["program"]}| Status: {student["status"]}|')
                    counter+=1
            if counter == 0:
                print("Status not found")
            return students, id
             