#WAPP to remove the duplicate from the list
List=[]
List_Even=[]
List_odd=[]
num=int(input("Enter the size of the list: "))
print("Enter values into the list: ")
for i in range(num):
    temp=int(input("Enter the value: "))
    List.append(temp)

print("List is: ",List)

for i in range(num):
    if (List[i]%2==0):
        List_Even.append(List[i])
    else:
        List_odd.append(List[i])

print("The New List with Even numbers: ",List_Even)
print("The New List with Odd numbers:", List_odd)