List=[]
List2=[]
num=int(input("Enter the size of the list: "))
for i in range(num):
    temp=input("Enter the Toy Name: ")
    List.append(temp)

print("List is: ",List)

for i in range(num):
    if List[i] not in List2:
        List2.append(List[i])

print("The New List without Duplicates is: ",sorted(List2))