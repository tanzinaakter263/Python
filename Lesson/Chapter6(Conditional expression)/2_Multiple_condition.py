age=int(input("Enter your age:"))

#if elif else ladder
if(age>=18):
  print("Yor are above the age of consent")   #space is called in indentation/indent
  print("Good for you")

elif(age<0):
  print("You are enter invalid  negative age")

elif(age==0):
  print("You are enter 0 which is not a valid age")
else:
  print("You are below the age of consent")



print("End of program")