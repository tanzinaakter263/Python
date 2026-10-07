f=open("file.txt")

#lines=f.readlines()  #readlines returns a list
#print(lines,type(lines))

line1=f.readline()  #readlines returns a list
print(line1,type(line1))
line2=f.readline()  #readlines returns a list
print(line2,type(line2))
line3=f.readline()  #readlines returns a list
print(line3,type(line3))
line4=f.readline()  #readlines returns a list
print(line4=="")


f.close()