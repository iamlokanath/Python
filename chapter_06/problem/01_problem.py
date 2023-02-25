# write a program in python to find the greatest of four numbers entered by the user
num1 = input("Enter the number 1: ")
num2 = input("Enter the number 2: ")
num3 = input("Enter the number 3: ")
num4 = input("Enter the number 4: ")
if(num1 > num2 and num1 > num3 and num1 > num4):
    print("num1")
elif(num2 > num1 and num2 > num3 and num2 > num4):
    print("num2")
elif(num3 > num1 and num3 > num2 and num3 > num4):
    print("num3")
elif(num4 > num1 and num4 > num2 and num4 > num3):
    print("num4")