class Employee:
  
  language = "Python"    # language,salary is a class attribute
  salary = 1200000

  def __init__(self,name,salary,language):  #dunder method which is automatically called
    self.name=name
    self.salary=salary
    self.language=language
    print("I am creating an object!!")

  def getInfo(self):
    print(f" the language is {self.language}. tha salary is {self.salary}")
  
  @staticmethod
  def greed():
    print("Good Morning")

tanzina=Employee("Tanzina",1300000,"JavaScript")    #tanzina is object
print(tanzina.name,tanzina.salary,tanzina.language)


