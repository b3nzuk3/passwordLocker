from username import User_name


def main():

    pm = User_name()

    print("""
    (1) Create a new user
    (2) Save accounts
    (3) Display accounts
    (4) Search existing contact
    (5) Delete saved account
    (q) Quit
    """)

    done = False

    while not done:
        
        choice = input("Enter your choice: ")
        if choice == "1":
            path = input("Enter new user name : ")
            pm.save_user(path)
            print()
            print()
        elif choice == "2":
            site = input(f"Enter the account name you would like to save {User_name.users[0]}: ")
            password = input(f"Please Enter the account password: ")
            pm.save_account(site, password)
            print()
            print()
        elif choice == "3":
            print(pm.display_contact())
            print()
            print()
        elif choice == "4":
            path = input(f"Enter the account to search for {User_name.users[0]}: ")
            print(pm.search_account(path))
        elif choice == "5":
            path = input(f"Enter the account you would like to Delete: ")
            print(pm.del_account(path))
            print()
            print()
        elif choice == "q":
            done = True
            print()
            print("Good Bye")
            print()
            print()
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
