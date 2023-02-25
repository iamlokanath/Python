# write a program in python yo find double spaces in a string
str = "I am   Lokanath"
doubleSpaces = str.find("  ")
str = str.replace("  ", " ")
print(str)