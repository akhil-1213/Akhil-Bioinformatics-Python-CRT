seq=input("Enter the DNA Sequence: ")
gc_per=((seq.count('G') + seq.count('C'))/len(seq))*100
print(gc_per,"%")
if gc_per>=60:
    print("Classification: High GC")
if gc_per>40 and gc_per<60:
        print("Classification: Moderate GC")
if gc_per<=40:
          print("Classification: Low GC")