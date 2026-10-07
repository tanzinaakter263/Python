class Employee:
  
  language = "Python"    # language,salary is a class attribute
  salary = 1200000


tanzina=Employee()    #tanzina is object
tanzina.name="Tanzina"  # this is an object/instance attribute
print(tanzina.name,tanzina.language,tanzina.salary)

jubydul = Employee()
jubydul.name="Jubydul Islam" 
print(jubydul.name,jubydul.salary,jubydul.language)


'''
Here name is object/instance attribute and salary,language is
class attribute as they direct belong to the class
'''