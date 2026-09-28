#Replace the double space from problem 3 with single space

name="Tanzina is a good girl and "
print(name.find("goo"))

name="Tanzina is a good  girl and "
print(name.replace("  "," "))
print(name) # Strings are immutable which means that you cannot change them by running functions on them
