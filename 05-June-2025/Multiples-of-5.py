#WAPP to read List from user and print a new list of numbers which are multiples of 5
List=[]
List2=[]
num=int(input("Enter the size of the list: "))
print("Enter values into the list: ")
for i in range(num):
    temp=int(input("Enter the value: "))
    List.append(temp)

print("List is: ",List)

for i in range(num):
    if (List[i]%5==0):
        List2.append(List[i])

print("The New List with Multiples of '5' is: ",List2)