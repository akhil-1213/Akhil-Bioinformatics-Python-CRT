username=input("Enter your name: ")
AZ_count=az_count=num_count=sp_count=0
while(1):
    user_contact=int(input("Enter your 10-digit contact number: "))
    user_mail=input("Enter a valid E-mail ID (ex-name@org.com): ")
    password=input("Enter your password: ")
    if len(str(user_contact))!=10 and user_mail.index('@')>user_mail.index('.'):
        print("Invalid Mail ID or Contact Number")
        break
    else:
        for i in range(len(password)):
            if password[i].isupper() and password[i].isalpha():
                AZ_count+=1
            elif password[i].islower() and password[i].isalpha():
                az_count+=1
            elif password[i].isnumeric():
                num_count+=1
            else:
                sp_count+=1
        if AZ_count>=3 and az_count>=3 and num_count>=1 and sp_count>=3 and len(password)==10:
            print("Your Details are valid")
            break
        else:
            print("Invalid.. Try Again")