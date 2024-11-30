from Employee import *
from Manager import *
from Worker import *
from FileHandling import *

def menu():
    filename = "employees.csv"
    while True:
        print("\nChoose the options:")
        print("1: Add Manager")
        print("2: Add Worker")
        print("3: Update Employee Information")
        print("4: Delete Employee")
        print("5: Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter manager's name: ")
            age = input("Enter manager's age: ")
            salary = input("Enter manager's salary: ")
            department = input("Enter manager's department: ")
            manager = Manager(name, age, salary, department)
            save_employee(filename, [manager.name, manager.get_age(), manager.get_salary(), manager.get_department(), ""],
                          ["Name", "Age", "Salary", "Department", "Hours Worked"])
        elif choice == "2":
            name = input("Enter worker's name: ")
            age = input("Enter worker's age: ")
            salary = input("Enter worker's salary: ")
            hours_worked = input("Enter worker's hours worked: ")
            worker = Worker(name, age, salary, hours_worked)
            save_employee(filename, [worker.name, worker.get_age(), worker.get_salary(), "", worker.get_hours_worked()],
                          ["Name", "Age", "Salary", "Department", "Hours Worked"])        
        elif choice == "3":
            headers, data = read_employees(filename)
            if data:
                emp_name = input("Enter the name to update: ")
                employee_found = False
                for row in data:
                    if row[0] == emp_name:
                        employee_found = True
                        print(f"Current details: {', '.join(row)}")
                        field = input(f"Select field to update ({', '.join(headers)}): ")
                        if field in headers:
                            value = input(f"Enter new value for {field}: ")
                            row[headers.index(field)] = value
                            update_csv(filename, [headers] + data)
                            print("Employee information updated.")
                        else:
                            print("Invalid name.")
                        break
                if not employee_found:
                    print(f"Employee with name '{emp_name}' not found.")
            else:
                print("No employees to update.")
        elif choice == "4":
            headers, data = read_employees(filename)
            if data:
                emp_name = input("Enter the name to delete: ")
                new_data = [row for row in data if row[0] != emp_name]
                if len(new_data) < len(data):
                    update_csv(filename, [headers] + new_data)
                    print(f"Employee '{emp_name}' deleted successfully.")
                else:
                    print(f"Employee with name '{emp_name}' not found.")
            else:
                print("No employees to delete.")        
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")
menu()
