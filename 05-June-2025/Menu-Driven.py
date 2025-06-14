'''add confirmed guets to list
   remove  a guest who cancels
   check if a friend is on list
   sort and print the final guest list
'''
Guest=[]
while(1):
    print("|---------------------MENU---------------------|")
    print("|1.Add confirmed guets.........................|")
    print("|2.Remove a Guest..............................|")
    print("|3.Check if a Guest attending party or not.....|")
    print("|4.View the Final Guest list...................|")
    print("|5.EXIT........................................|")
    print("|----------------------------------------------|")

    choice=int(input("enter your chioce:"))
    if(choice>=1 and choice<=5):
        if(choice==1):
            guestname=input("enter guest name:")
            Guest.append(guestname)
            print(f'{guestname} is added to guest list')
        elif(choice==2):
            cancelledguest=input("enter cancelled guest name:")
            if(cancelledguest in Guest):
             Guest.remove(cancelledguest)
             print(f'{cancelledguest} is removed from guest list')
            else:
               print(f'{cancelledguest} is not in  guest list')
        elif(choice==3):
            checkguest=input("enter guest name:")   
            if(checkguest in Guest):
              print(f'{checkguest} is attending')
            else:
               print(f'{checkguest} is not attending')
        elif(choice==4):
            if(len(Guest)==0):
              print("list is empty")
            else:
              Guest.sort()
              print("final list")
              print(Guest)
        else:
           print("---ENJOY PARTY---")
           break
    else:
       print("invalid input")