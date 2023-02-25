L1 = [1, 3, 6, 8, 9, 2, 4, 7]
# sort the list
L1.sort()
print(L1)
# reverse the list
L1.reverse()
print(L1)
# to add item to the list
L1.append(11)
print(L1)
# to insert a item by index
L1.insert(2, 90) #--> 2--> index 
print(L1)
#to remove the item by its index
L1.pop(3)
print(L1)
# to remove a iten by its value
L1.remove(2)
print(L1)
#print the number of particular item
print(L1.count(1))
L1[1] = 100
print(L1)