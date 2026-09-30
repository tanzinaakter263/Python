d={} #Empty dictionary

marks={
  "Harry":100,
  "Shivam":90,
  "Rohan":80,
  0:"Harry"
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry":98,"Renuka":100})
print(marks)
print(marks.get("Harry"))
print(marks.get("Shivika")) #None
print(marks["Harry"])

print(marks["Harry2"]) #Returns an error
print(marks.get("Harry2")) #Prints None but not error

