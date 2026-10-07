#Write a python fuction to print multiplication table a given number.

def multiply(n):
  for i in range(1,11):
    print(f"{n} X {i} = {n*i}")
n=int(input("Enter a number: "))
multiply(n)