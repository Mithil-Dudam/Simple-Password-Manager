print("Simple Password Manager!\n")
def inp():
    choice = input("Enter choice: ")
    if(choice.isdigit()):
        choice = int(choice)
        if(1 <= choice <=4):
            return choice
        else:
            print("Invalid input! Must be a number between 1 and 4.")
            return inp()
    print("Invalid input! Must be a valid option number.")
    return inp()

dict={}

def addPassword():
    website=input("Enter website name:  ").lower()
    username=input("Enter username: ")
    password=input("Enter password: ")
    dict[website]={"username":username,"password":password}
    print("\nPassword successfully saved!\n")

def getPassword():
    name = input("Enter website name: ")
    for key in dict:
        if key==name:
             return print(f"Password: {dict[name]['password']}\n")
    print("Website does not exist.\n")


def listPassword():
    if(len(dict)==0):
        print("No passwords stored.")
    for key,value in dict.items():
        print(f"website: {key} , password: {value['password']}")
    print()

def q():
    print("Thank you for using Password Manager!")
    exit()

while True:
    print("1. Add a new password")
    print("2. Retrieve password")
    print("3. List all passwords")
    print("4. Quit\n")

    choice = inp()

    if choice==1:
        addPassword()
    elif choice==2:
        getPassword()
    elif choice==3:
        listPassword()
    else:
        q()