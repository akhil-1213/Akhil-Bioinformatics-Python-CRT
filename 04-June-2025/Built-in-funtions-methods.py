#WAPP to read size of list as input and take the list elements as input and find the length of list 
# Maximum element present in the list
# Minimum
# Summation
# Sorted list in ascending order
n_size=int(input("Enter size of the list: "))
n_list=[]
for i in range(n_size):
    t=int(input(f"Enter {i+1} element into list: "))
    n_list.append(t)

print(n_list)
print(max(n_list))
print(min(n_list))
print(sum(n_list))
print(sorted(n_list))
n_list.reverse()
print(n_list)
n_list.insert(0,10)
print(n_list)
#Slicing
print(n_list[-1::])