#Write a python program which converts inches to cms.
def inch_to_cms(inches):
  return inches*2.54

n=int(input("Enter value in inches: "))
print(f"The corresponding value in cms is {inch_to_cms(n)}")