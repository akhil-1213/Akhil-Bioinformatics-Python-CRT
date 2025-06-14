#WAPP to read integer from user and find number of 0's present in the input
num=int(input("Enter the integer value: "))
num1=num
count=0
while(num>0):
    rem=num%10
    if(rem==0):
        count=count+1
    num=num//10

print(f"{num1} contains {count} zero's in it")