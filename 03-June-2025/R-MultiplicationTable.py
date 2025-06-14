#WAPP to print the reversed Multiplication Table of N
num=int(input("Enter the integer value: "))
for i in range(10,0,-1):
    print(f"{num}*{i} = ",num*(i))