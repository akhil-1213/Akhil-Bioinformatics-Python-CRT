#Python program to check whether the given number is a Digit or number
num=int(input("Enter the integer value:"))
if -9<=num<=9:
    print(f"{num} is Digit")
else:
    print(f"{num} is a Number")