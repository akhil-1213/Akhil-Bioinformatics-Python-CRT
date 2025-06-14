#WAPP to read a string and print count of
#-Upper vowels
#-Lower vowels
#-upper con
#-lower con
st=input("Enter your string: ")
uv=lv=uc=lc=0
for i in range(len(st)):
    if st[i] in "AEIOU":
        uv+=1
    elif st[i] in "aeiou":
        lv+=1
    elif st[i] not in "AEIOU" and st[i].isupper():
        uc+=1
    elif st[i] not in "aeiou" and st[i].islower():
        lc+=1
    else:
        print(f"{st[i]} is Not an Alphabet")

print("Uppercase vowels - ",uv)
print("Lowercase vowels - ",lv)
print("Uppercase Consonants - ",uc)
print("Lowercase Consonants - ",lc)