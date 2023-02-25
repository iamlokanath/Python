# a spam comment is defind as a texrt containsing following keywords
comment = input("Ener comment: ")
spam = False
if("Lot of money" in comment):
    spam = True
elif("Hello world" in comment):
    spam =True
elif("Lokanath" in comment):
    spam =True
else:
    spam = False
if(spam == True):
    print("The text is spam")
else:
    print("The text is not a spam")