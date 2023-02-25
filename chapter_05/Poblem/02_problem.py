# write a program in python to input eight numbers from theuser and display all the unique numbers

num1 = input("enter the number 1: ")
num2 = input("enter the number 2: ")
num3 = input("enter the number 3: ")
num4 = input("enter the number 4: ")
num5 = input("enter the number 5: ")
num6 = input("enter the number 6: ")
num7 = input("enter the number 7: ")
num = {num1, num2, num3, num4, num5, num6, num7}
print(type(num))
print("The unique numbers are", num)