from validations import validate_id_csv, validate_name_csv, validate_status_csv
from pathlib import Path
import csv

base = Path(__file__).parent.parent
path = base / "data" / "students.csv"

# This functions is used for saving the list of students in the program into a csv file
def save_csv(students, id):
    if students == []:
        print("There are no students to save")
    else:
        try:
            with open(path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["id", "name", "program", "status"])
                writer.writeheader()
                for student in students:
                    writer.writerow(student)
                
                print(f'Students csv file saved int path: {path}')
        
        except PermissionError:
            print("Error you have no rights to write in this file or it is in usage")
        except FileNotFoundError:
            print("Error: The path does not exists")
        except OSError as e:
            print(f'System error: {e}')
        except UnicodeDecodeError:
            print("UnicodeDecodeError")
        except Exception as e:
            print(f'Unexpected error: {e}')
    return students, id

def upload_csv(students, id):
    try:
        students_uploaded =[]
        invalid_rows = 0
        if students == []:
                with open(path, "r", newline="", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    if reader.fieldnames != ["id", "name", "program", "status"]:
                        print("Invalid headers in the uploaded file")
                        return [], id
                    else:
                        for student in reader:
                            local_dictionary = {}
                            try:
                                local_dictionary["id"] = validate_id_csv(students, student["id"])
                                local_dictionary["name"] = validate_name_csv(student["name"])
                                local_dictionary["program"] = validate_name_csv(student["program"])
                                local_dictionary["status"] = validate_status_csv(student["status"])
                                students_uploaded.append(local_dictionary)
                            except ValueError:
                                invalid_rows +=1
                        print(f'CSV file uploaded with: {invalid_rows} invalid rows')
                        return students_uploaded
    except PermissionError:
        print("Error you have no rights to read in this file or it is in usage")
    except FileNotFoundError:
        print("Error: The path does not exists")
    except OSError as e:
        print(f'System error: {e}')
    except UnicodeDecodeError:
        print("UnicodeDecodeError")
    except Exception as e:
        print(f'Unexpected error: {e}')        
