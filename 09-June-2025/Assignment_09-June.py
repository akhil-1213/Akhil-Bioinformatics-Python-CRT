input_string=input("Enter your String: ")

#[1]print string as list of characters
print(list(input_string))

#[2]Length of the string
print(len(input_string))

#[3]minimum element after converting string into list
print(min(list(input_string.replace(' ',''))))

#[4]find number of white spaces in the given string without using Built-in functions/methods
count=0
for i in range(len(input_string)):
    if(input_string[i]==" "):
        count=count+1
print(count)