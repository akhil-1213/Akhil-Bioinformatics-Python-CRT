n=input("Enter the DNA Sample: ")
#dna={'A':0,'T':0,'G':0,'C':0}
'''for i in range(len(n)):
    if n[i] not in "ATGC":
        print("Invalid sample")
        break
    else:
        if n[i]=='A':
            dna['A']+=1
        elif n[i]=='T':
            dna['T']+=1
        elif n[i]=='G':
            dna['G']+=1
        else:
            dna['C']+=1'''
dna={'A':n.count('A'),'T':n.count('T'),'G':n.count('G'),'C':n.count('C')}
print(dna)