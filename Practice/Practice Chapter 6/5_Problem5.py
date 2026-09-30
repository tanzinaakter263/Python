#Write a program to finds out whether a given number name is present in a list or not.

l=["Harry","Rohan","Shuvam","Divya"]
name=input("Enter your name:")
if(name in l):
  print("Your name is in the list")
else:
  print("Your name is not in the list")