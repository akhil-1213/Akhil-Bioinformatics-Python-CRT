#WAPP to read an integer from user and print number of even digits and odd digits
num=int(input("Enter the integer value: "))
num1=num
pos=0
neg=0
while(num!=0):
    rem=num%10
    if(rem%2==0):
        pos=pos+1
    else:
        neg=neg+1
    num=num//10

print(f"{num1} has {pos} even numbers and {neg} odd numbers")