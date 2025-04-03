class Employee:  #parent class
    def __init__(self,nm,sal):
        self.name=nm
        self.salary=sal
    def getnm(self):
        return self.name
    def getsal(self):
        return self.salary
    
class salesman(Employee):  #child class
    def __init__(self,nm,sal,inc):
        super().__init__(nm,sal)
        self.incentive=inc
    def getsal(self):
        return self.salary+self.incentive
    
e1=Employee('Shailesh',10000)
print(f'Total salary of a {e1.getnm()} is RS.{e1.getsal()}')
s1=salesman('Ram',8000,1500)
print(f'Total salary of {s1.getnm()} is Rs.{s1.getsal()}')