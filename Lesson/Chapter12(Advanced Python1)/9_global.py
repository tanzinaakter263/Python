a=89    #global variable

def func():
  global a     #global keyword change the global variable
  a=3     #local variable
  print(a)

func()
print(a)