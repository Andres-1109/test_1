from services.crud_services import add_student, delete_student, edit_student, show_students, search_students, exit_program
from services.csv_services import save_csv, upload_csv

def menu_options():
    return [
        {"option": "Add student", "action": add_student},
        {"option": "Delete student", "action": delete_student},
        {"option": "Edit student", "action": edit_student},
        {"option": "Show students", "action": show_students},
        {"option": "Search students", "action": search_students},
        {"option": "Save CSV", "action": save_csv},
        {"option": "Upload CSV", "action": upload_csv},
        {"option": "Exit", "action": exit_program},
    ]