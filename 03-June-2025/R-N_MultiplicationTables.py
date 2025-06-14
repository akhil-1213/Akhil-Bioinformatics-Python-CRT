#WAPP to print reversed Multiplication Table from N to 1
num=int(input("Enter the integer value: "))
for i in range(num+1,0,-1):
    for j in range(10,0,-1):
        print(f"{i}*{j} = ",(i)*(j))
    print("----Section----")