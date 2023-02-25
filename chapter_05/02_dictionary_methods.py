myDict = {
    "Mango": "A fruit",
    "Lokanath": "A boy",
    "Betira": "A Vilage",
    "Marks": [1,24,2],
    "anotherdict": {'orange': 'A color'}
}

print(myDict.keys()) # prints the keys of the dictionary
print(myDict.values()) #prints the keys of the dictionary
print(myDict.items()) # print the (key, value) for all contents of the dictionry


udateDict = {
    "Kanha": "Nick name of Lokanath",
    "Apple": "A nice fruit"
}
myDict.update(udateDict)  # Updates the dictionary by adding the key-value pairs frrom
print(myDict)