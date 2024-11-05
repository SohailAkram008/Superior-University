class Person:
    def info(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}")
class Employee:
    def info(self, emp_id, position):
        self.emp_id = emp_id
        self.position = position
    def display_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Position: {self.position}")
class Staff(Person, Employee):
    def __init__(self, name, age, emp_id, position, department):
        Person.info(self, name, age)
        Employee.info(self, emp_id, position)
        self.department = department
    def display_info(self):
        Person.display_info(self)
        Employee.display_info(self)
    def additional_info(self):
        print(f"Department: {self.department}")
staff_input = Staff("Sohail",20,31,"Student","DS")

staff_input.display_info()
staff_input.additional_info()
import os
import csv
def read_employee(file_CSV):
    employees = []
    with open(file_CSV, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:
                employees.append(Staff(row[0], (row[1]), row[2], row[3], row[4]))
    return employees
def add_employee(file_CSV, staff):
    with open(file_CSV, mode='a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([staff.name, staff.age, staff.emp_id, staff.position, staff.department])
def save_employees(file_CSV, employees):
    with open(file_CSV, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        for staff in employees:
            csv_writer.writerow([staff.name, staff.age, staff.emp_id, staff.position, staff.department])
file_CSV = "employees.csv"
add_employee(file_CSV, staff_input)
employees = read_employee(file_CSV)