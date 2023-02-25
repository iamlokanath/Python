# write a program in python to create a dictionary of Hindi words with values as their english translation and provide a option where user can look up
myDict = {
    "pankha": "Fan",
    "kursi": "chair",
    "khata": "Bed",
    "naam": "Name"
}

print("You can enter the following hindi words to know their english translation", myDict.keys())
a = input("Enter a hindi word from the abve option: ")
print("Means: ", myDict[a])

