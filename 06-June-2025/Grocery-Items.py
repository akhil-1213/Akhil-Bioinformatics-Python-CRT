#WAPP to declare a list of grocery items and read the input from user from 1 to 5
#-1 to display list of items in sorted way
#-2 to take input from user and add items to the cart
#-3 to view the cart items
#-4 to update the Quantity or Item present in the cart
#-5 Generate a bill including item names Item Quantity price and if the final bill amount is 
# greater than 1000 the user will get 10% discount
# if the user purcahses any item >10kg reduce the amount of 1kg from that particular item price
# if the user purchases any particular items add buy one and get one
# add 25% gst to overall bill and print the bill

Items=['A','B','C','D','E']
Prices=(200,220,240,300,350)
Cart=[]
Quantity=[]
Bill=0
while(1):
    print("|------------------MENU------------------------|")
    print("|1.Display - Items.............................|")
    print("|2.Add to cart.................................|")
    print("|3.Veiw cart items.............................|")
    print("|4.Cart Updation...............................|")
    print("|5.Billing.....................................|")
    print("|----------------------------------------------|")

    choice=int(input("enter your chioce:"))
    if(choice>=1 and choice<=5):
        if(choice==1):
           for i in range(len(Items)):
              print(f"{Items[i]}.................{Prices[i]}rs")
           print("---------------------------------------------")
        elif(choice==2):
           print(Items)
           place=int(input("Enter your choice of item**from 1-5**: "))
           Cart.append(Items[place-1])
           quantity=int(input("Enter the item Quantity: "))
           Quantity.append(quantity)
        elif(choice==3):
           print("Item......Quantity")
           for i in range(len(Items)):
              print(f"{Items[i]}.......{Quantity[i]}")
        elif(choice==4):
           update=int(input("Enter the item"))
        else:
           print("---ENJOY---")
           break
    else:
       print("invalid input")