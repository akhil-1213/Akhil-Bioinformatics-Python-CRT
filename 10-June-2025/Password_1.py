pswd=input("Enter your password: ")
AZ_count=az_count=num_count=sp_count=0
for i in range(len(pswd)):
    if pswd[i].isupper() and pswd[i].isalpha():
        AZ_count+=1
    elif pswd[i].islower() and pswd[i].isalpha():
        az_count+=1
    elif pswd[i].isnumeric():
        num_count+=1
    else:
        sp_count+=1

if AZ_count>=1 and az_count>=1 and num_count>=1 and sp_count>=1:
    print(f"{pswd} is a valid password")
else:
    print(f"{pswd} is not a valid password")