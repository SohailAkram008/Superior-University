# Company employe hierarchy
class Employee:
    def __init__(self, name,position):
        self.name = name
        self.position = position
    def display_info(self):
        print(f"Name: {self.name} Position: {self.position}")

class Manager(Employee):
    def __init__(self, name, position, department):
        super().__init__(name, position)
        self.department = department
    def additional_info(self):
        print(f"Name: {self.name} Position: {self.position} Department: {self.department}")

class Worker(Employee):
    def __init__(self, name, position, hour_worked):
        super().__init__(name, position)
        self.hour_worked = hour_worked
    def additional_info(self):
        print(f"Name: {self.name} Positon: {self.position} Hour Worked: {self.hour_worked}")

employee = Employee("Haroon", "Dean")
employee.display_info()
manager = Manager("Muskan", "Data Engineer", "IT")
manager.additional_info()
worker = Worker("Baber", "Administration", 6)
worker.additional_info()