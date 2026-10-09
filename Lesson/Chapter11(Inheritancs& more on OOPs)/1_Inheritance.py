class Employee:  #Base class or Parent Class
  company="ITC"
  def show(self):
    print(f"The name is {self.name} and the salary is {self.salary}")
class programmer(Employee):   #Inherited Class
  company = "ITC Infotech"
  
  def showLanguage(self):
      print(f"The name is {self.name} and he good is with  {self.language}")


a=Employee()
b=programmer()
print(a.company,b.company)