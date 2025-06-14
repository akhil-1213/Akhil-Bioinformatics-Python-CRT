#WAPP input=amount and print the number of notes  required in Indian currency Dimension
amt=int(input("Enter the amount: "))
print("2000---->",amt//2000)
amt=amt%2000
print("500---->",amt//500)
amt=amt%500
print("200---->",amt//200)
amt=amt%200
print("100---->",amt//100)
amt=amt%100
print("50---->",amt//50)
amt=amt%50
print("20---->",amt//20)
amt=amt%20
print("10---->",amt//10)
amt=amt%10
print("5---->",amt//5)
amt=amt%5
print("2---->",amt//2)
amt=amt%2
print("1---->",amt//1)
amt=amt%1