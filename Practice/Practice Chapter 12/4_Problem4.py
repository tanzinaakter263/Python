#Write a program to display a/b where a and b are integers.if b==0 display infinite by handling the 'ZeroDivisionError'.

try:
  a=int(input("enter a number: "))
  b=int(input("enter a number: "))
  print(a/b)
except ZeroDivisionError as v:
  print("Infinite")