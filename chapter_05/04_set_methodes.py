# we can not change items in he set


b = set()
print(type(b))
b.add(2)
b.add(3)
b.add(3) # Adding a value repeatedly does not change a set
b.add(7)
b.add(6)
print(b) # set always gives the output in a assending manner

#In set we can not add list or dictionary

print(len(b)) # Print the length (number of elements) of the set

b.remove(2) # remove the element that you have put inside the remove()
print(b) 
 
print(b.pop()) #it will remove a aribitary value

b.clear()
print(b)

s1 = {12, 13}
s2 = s1.union({11, 14})
print(s2)
s3 = s1.intersection({12, 15})
print(s3) 