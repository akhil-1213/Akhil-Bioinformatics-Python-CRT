#WAPP to integer from user and find summation of even digits and odd digits present in that input
num=int(input("Enter the integer value: "))
num1=num
pos=0
neg=0
while(num!=0):
    rem=num%10
    if(rem%2==0):
        pos=pos+rem
    else:
        neg=neg+rem
    num=num//10

print(f"{num1} has {pos} even total and {neg} odd total")