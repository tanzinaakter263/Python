#write a program to great all the persons named stored in a list "l" which start with S

l=["Harry","Shuvam","Rohan","Sachin"]
for name in l:
  if(name.startswith("S")):
    print(f"Hello {name}")