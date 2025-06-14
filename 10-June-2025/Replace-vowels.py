#WAPP to read a string as input and replace all vowels with 0's
st=n=input("Enter string: ")
for i in st:
    if i in "AEIOUaeiou":
        n=n.replace(i,'0')
print(n)