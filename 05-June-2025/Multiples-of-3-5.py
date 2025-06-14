#WAPP to read list from user and check whether the list elements are multiples of 3 and 5 or not and print the list of elements which are multiples of 3 and 5
List=[]
List2=[]
num=int(input("Enter the size of the list: "))
print("Enter values into the list: ")
for i in range(num):
    temp=int(input("Enter the value: "))
    List.append(temp)

print("List is: ",List)

for i in range(num):
    if ((List[i]%5==0) or (List[i]%3==0)):
        List2.append(List[i])

print("The New List with Multiples of '5' is: ",List2)