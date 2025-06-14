#WAPP to read a string as input and print no. of
#-uppercase leters
#-lowercase letters
#-numeric values
#-special characters
qwer=input("Enter the string: ")
up=lo=nu=sp=0
for i in range(len(qwer)):
    if qwer[i].isupper():
        up+=1
    elif qwer[i].islower():
        lo+=1
    elif qwer[i].isnumeric():
        nu+=1
    else:
        sp=+1

print(up,lo,nu,sp)