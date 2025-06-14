Food=["Dum-Biryani","Fry-Biryani","Chicken-Majestic","Dragon-Chicken","Chicken-Lollipop-Biryani"]
Prices=(200,220,240,300,350)
Food_Order=[]
Quantity=[]
Bill=0
while(1):
    print("|------------------MENU------------------------|")
    print("|1.Display - Menu of Food of Items.............|")
    print("|2.Take Order from User........................|")
    print("|3.Billing.....................................|")
    print("|4.Confirm and Deliver Bill....................|")
    print("|5.EXIT........................................|")
    print("|----------------------------------------------|")

    choice=int(input("enter your chioce:"))
    if(choice>=1 and choice<=5):
        if(choice==1):
           for i in range(len(Food)):
              print(f"{Food[i]}.................{Prices[i]}rs")
           print("-------------------------------------")
        elif(choice==2):
           while(1):
              print(Food)
              order=int(input("Please place your order: **press 0 if done ordering**"))
              quantity=int(input("Please enter the quantity of your order: "))
              Food_Order.append(Food[order])
              Quantity.append(quantity)
              if(order==0):
                 break
        elif(choice==3):
           for i in range(len(Food_Order)):
              if Food_Order[i+1] in Food:
                 index=Food.index(Food_Order[i+1])
                 Bill=Bill+(Prices[index]*Quantity[i+1])
        elif(choice==4):
           gst=Bill+(Bill*0.18)
           print(f"Your Total Bill amount is {Bill}rs")
        else:
           print("---ENJOY---")
           break
    else:
       print("invalid input")