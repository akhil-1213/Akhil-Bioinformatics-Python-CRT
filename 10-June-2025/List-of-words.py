#WAPP to read sentence as input and print list of words from the sentence
sen=input("Enter your sentence: ")
for ch in range(len(sen)-1):
    if(sen[ch+1]==" "):
        print()
    else:
        print(sen[ch],end="")