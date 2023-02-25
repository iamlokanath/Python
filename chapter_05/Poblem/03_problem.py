# create an emty dictionary. Allows four friends to enter thier fav lang as values and name as key

s1 = input("enter friend1 name: ")
s2 = input("enter friend2 name: ")
s3 = input("enter friend3 name: ")
s4 = input("enter friend4 name: ")
sn = {s1,s2,s3,s4}
s5 = input("enter friend1 fav color: ")
s6 = input("enter friend2 fav color: ")
s7 = input("enter friend3 fav color: ")
s8 = input("enter friend4 fav color: ")
sc = {s5, s6, s7, s8}

myDict = {
    s1 : s5,
    s2 : s6,
    s3 : s7,
    s4 : s8,
    
}
print(myDict)