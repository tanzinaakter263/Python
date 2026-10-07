class Employee:
  
  language = "Python"    # language,salary is a class attribute
  salary = 1200000

  def __init__(self):  #dunder method which is automatically called
    print("I am creating an object!!")

  def getInfo(self):
    print(f" the language is {self.language}. tha salary is {self.salary}")
  
  @staticmethod
  def greed():
    print("Good Morning")

tanzina=Employee()    #tanzina is object
tanzina.name="Tanzina"
print(tanzina.name,tanzina.salary)


jubydul=Employee()