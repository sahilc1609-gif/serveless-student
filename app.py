import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from database import initialize_database
from students import add_student, list_students, delete_student
from results import add_result, show_result, all_results

def menu():
    print("\n" + "="*50)
    print(" SERVERLESS STUDENT RESULT MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Add Result")
    print("5. View Student Result")
    print("6. View All Results")
    print("7. Exit")

def main():
    initialize_database()
    while True:
        menu()
        choice = input("Enter choice: ").strip()
        if choice == "1": add_student()
        elif choice == "2": list_students()
        elif choice == "3": delete_student()
        elif choice == "4": add_result()
        elif choice == "5": show_result()
        elif choice == "6": all_results()
        elif choice == "7":
            print("Goodbye!"); break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()
