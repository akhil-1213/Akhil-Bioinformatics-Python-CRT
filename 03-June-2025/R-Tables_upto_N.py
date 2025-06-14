#WAPP to print reverse multiplivation table from 1 to N
num=int(input("Enter the integer value: "))
for i in range(1,num+1):
    for j in range(10,0,-1):
        print(f"{i}*{j} = ",(i)*(j))
    print("----Section----")