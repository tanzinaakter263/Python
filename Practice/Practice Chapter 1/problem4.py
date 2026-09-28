"""write a python program to print the contents of a directory 
using the os module. Search online
 for the function which does that."""


import os

# Specify the directory path
directory = "/"

# Get the contents of the directory
contents = os.listdir(directory)

# Print the contents
for item in contents:
    print(item)
