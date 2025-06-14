List=[]
List2=[]
num=int(input("Enter the size of the list: "))
print("Enter Nmaes into the list: ")
for i in range(num):
    temp=(input("Enter the Student: "))
    List.append(temp)

print("List of Students: ",List)

temp=List[3]
List[3]=List[4]
List[4]=temp

print("The New List after Shuffling is: ",List)