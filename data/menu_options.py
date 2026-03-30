def menu_options():
    return [
        {"option": "Add student", "action": add_student},
        {"option": "Delete student", "action": delete_student},
        {"option": "Edit student", "action": edit_student},
        {"option": "Search student", "action": search_student},
        {"option": "Save CSV", "action": save_csv},
        {"option": "Upload CSV", "action": upload_csv},
        {"option": "Exit", "action": exit_program},
    ]