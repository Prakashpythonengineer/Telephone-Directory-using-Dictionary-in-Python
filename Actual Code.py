#Implement a Telephone Directory using Dictionaries
print("                 Welcome To Telephone Directory")
print("\n")
print("      Press 1 to Create Name with the respective number")
print("      Press 2 to Search the phone number using Name")
print("      Press 3 to Search the name using Phone number")
print("      Press 4 to Print the total number of entries")
print("      Press 5 to Modify existing data")
td={}
ct='y'
while ct=='y':
    choice=int(input("Enter your Choice:"))
    if choice==1:
        print("Enter the Name with the respective phone numeber")
        name=input("Enter the Name:")
        ph_no=int(input("Enter the Phone number:"))
        td[ph_no]=name
        print("Successfully Created :)")
    elif choice==3:
        number=int(input("Enter the Phone number"))
        for n in td:
            if number==n:
                print("The Name is present in the Telephone Directory")
                print("The Name is :",td[n])
    elif choice==2:
        n=input("Enter the Name:")
        for i in td:
            if td[i]==n:
                print("The Phone number is present in the Telephone Directory")
                print("The Phone number is:",i)
                break
        else:
            print("The Phone Number is not there!!")
    elif choice ==4:
        print("The Total number of Enteries are:",len(td))
    elif choice ==5:
        n=int(input("Enter the Phone number to change the name"))
        for i in td:
            if i==n:
                na=input("Enter the name:")
                td[i]=na
                print("Successfully Changed!!")
                break 
        else:
            print("The Phone number is not there!")

    ct=input("Do you want to Continue (y/n) ")
print("\nThanks for Choosing our Service")
