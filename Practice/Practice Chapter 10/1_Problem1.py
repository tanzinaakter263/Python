#Create a class "Programmer" for storing information of few programmers working of Microsoft.

class Programmer:
  company="Microsoft"

  def __init__(self,name,salary,pin):
    self.name=name
    self.salary=salary
    self.pin=pin

p=Programmer("tanzina",1200000,12345)
print(p.name,p.salary,p.pin,p.company)

j=Programmer("Jubydul",1300000,1234521)
print(j.name,j.salary,j.pin,j.company)