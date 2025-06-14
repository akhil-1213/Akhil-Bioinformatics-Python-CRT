#WAPP to take name as input including prefix as Mr/Ms and print the gender classification of the name
st=input("Enter the name: ")
if st.startswith('Mr'):
    print("Male")
elif st.startswith('Ms'):
    print("Female")
else:
    print("Irrelavent")