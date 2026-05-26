class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)

Student.show_school()

class Employee:

    company = "Google"

    # Class Method 

    @classmethod
    def change_company(cls, name):
        cls.company = name

    # Static method 

    @staticmethod
    def greet():
        print("Welcome Employee")


Employee.greet()

Employee.change_company("Microsoft")

print(Employee.company)

