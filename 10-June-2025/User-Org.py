#WAPP to read mail-id as input from user and print username and organisation name 
mail_id=input("Enter mail ID: ")
'''lis_name=mail_id.split('@')
lis_org=lis_name[1].split('.')
print(lis_name[0],lis_org[0])'''
print("Username = ",mail_id[0:mail_id.index('@'):])
print("Organization  = ",mail_id[mail_id.index('@')+1:mail_id.index('.')])