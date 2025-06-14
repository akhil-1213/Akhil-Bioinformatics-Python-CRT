#WAPP to read integer as input from user and find the summation of digits
num=int(input("Enter the integer value: "))
num1=num
#num=abs(num)
c=0
while(num*-1<0):
    rem=num%10
    num=num//10
    c=c+rem

print(f"Sum of digits in {num1} is {c}")