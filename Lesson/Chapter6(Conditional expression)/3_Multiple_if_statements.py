age=int(input("Enter your age:"))

#if statement no. 1 Independent condition
if(age%2==0):
  print("Age is even")
#End of if statement no. 1 Independent condition
#if elif else ladder
#if statement no. 2 Independent condition
if(age>=18):
  print("Yor are above the age of consent")   #space is called in indentation/indent
  print("Good for you")

elif(age<0):
  print("You are enter invalid  negative age")

elif(age==0):
  print("You are enter 0 which is not a valid age")
else:
  print("You are below the age of consent")
#End of if statement no. 2 Independent condition


print("End of program")