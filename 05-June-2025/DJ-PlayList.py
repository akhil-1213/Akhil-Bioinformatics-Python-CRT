List=[]
List2=[]
num=int(input("Enter the Number of songs: "))
for i in range(num):
    temp=input("Enter the Song Name: ")
    List.append(temp)

print("List of Songs: ",List)
List.reverse()
print("New Song list is: ",List)