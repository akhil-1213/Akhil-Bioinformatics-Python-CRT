#WAPP to read interger from user and print Multiplication Table of it
num=int(input("Enter the integer value: "))
for i in range(10):
    print(f"{num}*{i+1} = ",num*(i+1))