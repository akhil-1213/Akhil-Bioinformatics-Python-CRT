#WAPP to build a function ehich prints the multiplication table of n
def m_table(num):
    for i in range(10):
        print(f"{num}*{i+1} = ",num*(i+1))
n=int(input("Enter your value: "))
m_table(n)