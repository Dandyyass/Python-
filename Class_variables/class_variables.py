# Employee Class
# This program creates employee objects and applies a raise.

class Employee:
    def __init__(self, name, last, age, pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay

emp_1 = Employee("Carl", "Jung", "32", 5000)
emp_2 = Employee("Sigmund", "Freud", "22", 3000)

print(emp_1.__dict__, "\n", emp_2.__dict__)



class Employee2:
    raise_percent = 1.10  # 10% raise 

    def __init__(self, name, last, age, pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay

    def full_name(self):
        return "{} {}".format(self.name, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_percent)

    def info(self):
        print("Name : {} {}".format(self.name, self.last))
        print("Age  : {}".format(self.age))
        print("Pay  : ${}".format(self.pay))
        print("-------------------")


emp_3 = Employee2("John", "Smith", 30, 5000)
emp_4 = Employee2("Sara", "Jones", 25, 4000)

print("\n=== Before Raise ===")
emp_3.info()
emp_4.info()

emp_3.apply_raise()
emp_4.apply_raise()

print("=== After Raise ===")
emp_3.info()
emp_4.info()