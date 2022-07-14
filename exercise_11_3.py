class Employee():
    def __init__(self,name,sername,year_salary):
        """create attribute name,sername,year_salarry"""
        self.name=name
        self.sername = sername
        self.year_salary = year_salary

    def give_raise(self,increase=5000):
        """default value increase = 5000"""
        self.increase = increase
        self.salary=self.year_salary+self.increase
        return self.salary

