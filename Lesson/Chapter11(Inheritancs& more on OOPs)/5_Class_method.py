class Employee:
  a=1
  @classmethod   #Print class attribute instead of instance attribute because @classmethod
  def show(self):
    print(f"The class value of a is {self.a}")

e=Employee()
e.a=45

e.show()