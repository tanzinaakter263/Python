def main():

  try:
    a=int(input("Enter e number: "))
    print(a)


  except Exception as e:
    print(e)

  finally:
   print("I am inside of finally")

main()