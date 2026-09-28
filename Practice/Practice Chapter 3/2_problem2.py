#Write a program to fill in a letter template given below with name and date.

letter = ''' Dear <|Name|>
You are selected!
<|Date|>
'''
print(letter)
print(letter.replace("<|Name|>","Tanzina").replace("<|Date|>","20 September,2026"))
