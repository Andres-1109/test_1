from pathlib import Path
import csv

base = Path(__file__).parent.parent
path = base / "data" / "students.csv"


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