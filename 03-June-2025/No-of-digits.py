#WAPP to read input as integer from user and find number of digits present in that number
num=int(input("Enter the integer value: "))
num1=num
#num=abs(num)
c=0
while(num*-1<0):
    num=num//10
    c+=1

print(f"{num1} has {c} digits")