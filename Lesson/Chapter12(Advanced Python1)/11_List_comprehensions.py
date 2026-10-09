myList=[1,2,5,9,3,5]

'''squaredList=[]
for item in myList:
  squaredList.append(item*item)
'''
#Simplied using list comprehensions

squaredList=[i*i for i in myList]

print(squaredList)