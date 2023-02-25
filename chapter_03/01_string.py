greeting = "Good Morning"
name = "Lokanath"

# Concatinate two strings
print(greeting + name)

# printing the string by its index
print(name[0])

# slicing a string
print(name[0:3])
print(name[0:]) # same as print(name[0:8])
print(name[:8]) # same as print(name[0:8])

# slicing string by negative index
print(name[-8:-1])

# slicing with skip value
print(name[0:8:2]) # 0 --> from 8 --> to 2--> number of index to skip 2 means 1 