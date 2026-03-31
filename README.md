## Students management system with data persistance in CSV

1) How to run the program:
    
    This program should always be initialized from main.py for it to run properly.

2) Which features does the program includes?:

    This program have 8 different features that are listed and described below:

        1. Add student:

                This function is used to add a new student to the list of students it will ask the user for:
                    -Name
                    -Program
                    -Status
                And it will automatically add the ID based on and internal list to don't get any repteaded ID.

        2. Delete student:

                This function is used to delete an student from the list of students it will show you the current list of students and asks the user for the number of the student 
                that you want to delete.
        
        3. Edit student:

                This function asks the information to edit:
                    -Name
                    -Program
                    -Status
                The ID remains equal as the starting one.

        4.  Show students:

                This function shows the students that appear in the list.

        5. Search student:

                This function asks the user for how the user would like to search for the students, it gives him 4 option:
                    -ID
                    -Name
                    -Program
                    -Status

        6. Save CSV: 

                This function converts the list of students into a csv file to get persistance of the data, so it can be used when running the program again.

        7. Upload CSV: 

                This function converts a csv file into a list of students so it can later be used to be edited when using the program. By now this only works with a local initial empty students dictionary

        8. Exit program:

                This function is used to close the program and gives a brief good bye message to the user.
        
3) Usage example:
        
        This program can be used to managa the data of a students by entering the options on the menu to select the action to execute. It can be used to save data that could be used later whe running the program again and also upload an existing csv file to upload it.