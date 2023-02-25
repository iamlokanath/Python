# write a python program to find out weather a given username contains less than 10 characters or not
username = input("Enter Your Name: ")
if(len(username) < 10):
    print("username contains less than 10 characters")
else:
    print("Username contains more than 10 characters")