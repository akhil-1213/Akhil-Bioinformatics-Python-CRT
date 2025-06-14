'''
WAPP to read marks of 5 students for 3 subjects each and print the Marks List 
for Induvidual Students along with the class where '''
# if student marks>90 = 1st class
# >75 = 2nd class
# >50 = 3rd class
# <50 Fail

Subject1=[]
Subject2=[]
Subject3=[]
stu=int(input("Enter the Number of Students: "))
for i in range(3):
    for j in range(stu):
        temp=int(input(f"Enter Student{j+1} marks in Subject{i+1}: "))
        if(i==0):
            Subject1.append(temp)
        elif(i==1):
            Subject2.append(temp)
        elif(i==2):
            Subject3.append(temp)
    print("----------*****----------")

print("|S1,S2,S3,S4,S5|")
print(Subject1)
print(Subject2)
print(Subject3)