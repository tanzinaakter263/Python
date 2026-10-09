#Write a program name to input name,marks and phone number of a student and format it using the format function .

name=input("Enter a name: ")
marks=int(input("enter a marks: "))
phone=int(input("Enter a phone number: "))

s="The name of the student is {}, marks are {} and phone number is {}".format(name,marks,phone)
print(s)

