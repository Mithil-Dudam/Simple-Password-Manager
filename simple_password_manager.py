websites = {}

print("Simple Password Manager!\n")


def get_user_inp():
    choice = input("Enter choice (1,2,3,4): ")
    if choice in ["1", "2", "3", "4"]:
        return int(choice)
    return get_user_inp()


def addPassword():
    website = input("\nEnter website name:  ").strip()
    if website.lower() in websites:
        return print(f"{website} already exists.\n")
    password = input("Enter password: ")
    websites[website] = password
    return print("\nPassword successfully saved!\n")


def getPassword():
    if not websites:
        return print("No passwords stored.\n")
    website = input("Enter website name: ").strip()
    if website in websites:
        return print(f"Password: {websites[website]}\n")
    return print(f"{website} does not exist.\n")


def listPassword():
    if not websites:
        return print("No passwords stored.\n")
    for website in websites:
        print(f"website: {website} , password: {websites[website]}")
    print()


while True:
    print("1. Add a new password")
    print("2. Retrieve password")
    print("3. List all passwords")
    print("4. Quit\n")

    choice = get_user_inp()

    match choice:
        case 1:
            addPassword()
        case 2:
            getPassword()
        case 3:
            listPassword()
        case 4:
            print("Thank you for using Password Manager!")
            exit()
