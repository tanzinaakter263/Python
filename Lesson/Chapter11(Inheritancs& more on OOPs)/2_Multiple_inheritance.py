class Employee:  #Base class or Parent Class
  company="ITC"
  name="Tanzina"
  def show(self):
    print(f"The name is {self.name} and the company is {self.company}")

class coder:
   language="Python"
   def printLanguage(self):
      print(f"Out of all the language here is your language: {self.language}")

class programmer(Employee,coder):   #Inherited Class
  company = "ITC Infotech"
  
  def showLanguage(self):
      print(f"The name is {self.company} and he good is with  {self.language}")


a=Employee()
b=programmer()

b.show()
b.printLanguage()
b.showLanguage()