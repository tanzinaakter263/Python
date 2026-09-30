#If the 2 friends name are same;what will be the program in problem6?
#Value can be same but key should be unique. So if the name is same then the value will be updated with the new value.
d={}
name=input("Enter friends name: ")
lang=input("Enter Language name: ")
d.update({name:lang})
name=input("Enter friends name: ")
lang=input("Enter Language name: ")
d.update({name:lang})
name=input("Enter friends name: ")
lang=input("Enter Language name: ")
d.update({name:lang})
name=input("Enter friends name: ")
lang=input("Enter Language name: ")
d.update({name:lang})
print(d)