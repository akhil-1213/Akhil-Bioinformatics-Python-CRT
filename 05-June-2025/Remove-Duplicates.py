#WAPP to remove the duplicate from the list
List=[]
List2=[]
num=int(input("Enter the size of the list: "))
print("Enter values into the list: ")
for i in range(num):
    temp=int(input("Enter the value: "))
    List.append(temp)

print("List is: ",List)

for i in range(num):
    if List[i] not in List2:
        List2.append(List[i])

print("The New List without Duplicates is: ",List2)