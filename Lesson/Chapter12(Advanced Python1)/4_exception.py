try:
    a=int(input("Enter e number: "))
    print(a)

except ValueError as v:
    print("hiii!")
    print(v)

except Exception as e:
    print(e)

print("Thank you!")