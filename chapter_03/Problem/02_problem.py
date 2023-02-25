# wrirte a program to fill in a letter template given below with name and date
letter =  '''Dear <|NAME>|
You are selected
Date : <|DATE>|
'''
name = input("Enter your Name: ")
date = input("Enter Date: ")
letter = letter.replace("<|NAME>|", name)
letter = letter.replace("<|DATE>|", date)
print(letter)