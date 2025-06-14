#WAPP to crate a tuple of names and print the origial tuple and print The names which has a length of 5 from the tuple
tuple=('a','badko','c','d','e','f','g','h','i','jagadeesh')
print(tuple)
for i in range(len(tuple)):
    if(len(tuple[i])>=5):
        print(tuple[i])