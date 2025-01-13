# this file contain the oops concepts.
from time import sleep


class Employee:
    company = "techCorp"

    # Initializer / Instance attributes
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    # Instance method.
    def display_info(self):
        return f"ID:{self.emp_id},name:{self.name},Salary: {self.salary}"


# Create objects

emp1 = Employee(1, "Alice", 100000);
emp2 = Employee(2, "Bob", 20000);

# Access attributes and methods

print(emp1.display_info())
print(emp2.display_info())


# 2. Inheritance
class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    # Overriding the display_info method
    def display_info(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}, Department: {self.department}"


# Create object
mgr1 = Manager(3, "Charlie", 80000, "IT")
mgr2 = Manager(4, "amit", 40000, "HR")

print(mgr2.display_info())
# Access attributes and methods
print(mgr1.display_info())  # ID: 3, Name: Charlie, Salary: 80000, Department: IT


# 3. Polymorphism

class Developer(Employee):
    def __init__(self, emp_id, name, salary, programming_language):
        super().__init__(emp_id, name, salary)
        self.programming_language = programming_language

    # overriding the display method.
    def display_info(self):
        return (f"ID:{self.emp_id},Name:{self.name},Salaryies:{self.salary},"
                f"ProgramingLanguage:{self.programming_language}")


dev1 = Developer(1, "Palaki", 20000, "python")

print(dev1.display_info())

#4. Encapsulation

class Employee1:
    company = "TechCorp"

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.__salary = salary  # Private attribute

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary")

    def display_info(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.__salary}"

# Create object
emp1 = Employee1(1, "Employee1:Alice", 50000)

# Access private attribute using getter
print(emp1.get_salary())  # 50000

# Modify private attribute using setter
emp1.set_salary(55000)
print(emp1.get_salary())  # 55000