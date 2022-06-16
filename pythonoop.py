# create class
# name, salary, department
class Employee:
    # create method
    def __init__(self, name, salary, department): #constructor
        self.name = name
        self.salary = salary
        self.department = department
    
    def Showdata(self):
        print("name = {}".format(self.name))
        print("salary = {}".format(self.salary))
        print("department = {}".format(self.department))

# create oblect
obj1 = Employee("jen", 100000, "sale")
obj2 = Employee("li", 40000, "pro")

# use method
obj1.Showdata()
obj2.Showdata()
