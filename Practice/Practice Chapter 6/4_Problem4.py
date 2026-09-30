#Write a program to find weather a given user name contains less than 10 charcters or not .

username=input("Enter username:")

if(len(username)<10):
  print("user name contains less than 10 characters")

else:
  print("All is well! user name contains more than  or equal to 10 characters")