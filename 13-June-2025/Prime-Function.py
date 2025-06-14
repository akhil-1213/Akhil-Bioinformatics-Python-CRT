#WAPP to check whether the user given integer is prime or not using functions - use "return"
def prime(num):
    c=0
    for i in range(num):
        if(num%(i+1)==0):
            c+=1
    if(c==2):
        return "Prime"
    else:
        return "Not Prime"
    
n=int(input("Enter the integer value: "))
print(prime(n))