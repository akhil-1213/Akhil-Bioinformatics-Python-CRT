mut=[]
n=1
while(n>0):
    seq1=input("Enter your sequence1: ")
    seq2=input("Enter your sequence2: ")
    if(len(seq1)==len(seq2)):
     for i in range(len(seq2)):
           if(seq1[i]!=seq2[i]):
            mut.append(i)
     n=0
    else:
        print("Seq Mismatch")
print(mut)