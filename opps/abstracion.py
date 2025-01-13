# 5. Abstraction
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    @abstractmethod
    def display_info(self):
        pass


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display_info(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}, Department: {self.department}"


class Developer(Employee):
    def __init__(self, emp_id, name, salary, programming_language):
        super().__init__(emp_id, name, salary)
        self.programming_language = programming_language

    def display_info(self):
        return (f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary},"
                f" Programming Language: {self.programming_language}")


# Create objects
mgr1 = Manager(3, "Charlie", 80000, "IT")
dev1 = Developer(4, "Dave", 70000, "Python")

# Access methods
print(mgr1.display_info())  # ID: 3, Name: Charlie, Salary: 80000, Department: IT
print(dev1.display_info())  # ID: 4, Name: Dave, Salary: 70000, Programming Language: Python
