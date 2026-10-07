class Employee:
  
  language = "Python"    # language,salary is a class attribute
  salary = 1200000

  def getInfo(self):
    print(f" the language is {self.language}. tha salary is {self.salary}")
  
  @staticmethod
  def greed():
    print("Good Morning")

tanzina=Employee()    #tanzina is object
#tanzina.language="JavaScript"


tanzina.getInfo()
tanzina.greed()