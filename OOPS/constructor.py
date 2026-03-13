class Employee:
    def __init__(self,name,salary,company):
        self.name=name
        self.salary=salary
        self.company=company
    def get_salary(self):
        return self.salary
    
    def comp(self):
        return self.company
    def info(self):
        print(f"employee name is {self.name} company is {self.company} and salary is {self.salary}")
e1=Employee("govind",3200,"tcs")
print(e1.info())
e2=Employee("nikhil",3,"tcs")
print(e2.info())


    