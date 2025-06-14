#Python program to check whether the number is Positive or Negetive
num=int(input("Enter the integer value: "))
if(num>0):
    print(f"{num} is a positive number")
elif(num<0):
    print(f"{num} is a negetive number")
else:
    print(f"{num} is 0")