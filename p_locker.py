import pyperclip
from user import User
#To add an account
def create_account(account,username,password):
    '''
    Function to create a new account
    '''
    new_user = User(account,username,password)
    return new_user
#To save a user
def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()
#To find user
def find_user(account):
    '''
    Function to find user
    '''
    return User.find_by_account(account)
#To check existing user
def check_existing_user(account):
    '''
    Function to check existing user
    '''
    return User.user_exist(account)
#To display users
def display_users():
    '''
    Function to display users
    '''
    return User.display_users()

#------------------------------------------------------------
def main():
    print("\033[1;36;40m PASSWORD LOCKER\n")
    print("")
    prom = input("Welcome ,please enter your name: ")
    print("  ")
    print("Hello, " + prom + ", please make a selection below")
    print(" ")
    print("\033[1;34;1m  Options On how to Get Started on Password Locker\n")
    print("")
    # print("\033[1;35;1m cc -> To Create an Account\n")
    # print("\033[1;35;1m Log -> To log in\n")
    # print("\033[1;35;1m ex -> Exit\n")
    while True:
        print("Use these short codes : \n cc - create an account\n dc - print a list of saved credentials\n fc - find a user\n ex - exit navigation ")
        print(" ")
        short_code = input('Enter : ').lower().strip()
        if short_code == 'cc':
            print('To create a new account: ')
            first_name = input("Enter the first name: ")
            last_name = input("Enter your last name: ")
            password = input("Enter your password: ")
            print("\033[1;32;1m  \n")
            print( first_name +" "+ last_name + " You have successfully signed in to Password Locker using password " + password)
            print("-------------- ")
            print("To save an account, Enter the respective credentials :  ")
            print("--------------ssss")
            account = input("Enter the name of the account that you want to store:  ")
            username = input("Enter the username you are using:  ")
            password = input("Enter your password:  ")
            save_user(User(account, username, password ))
            print("\033[1;31;1m You have successfully saved your Credentials \n")
            # print(emoji.emojize('Python is :thumbs_up_sign:'))
            print("\033[1;32;1m  \n")
        elif short_code == "dc":
            if display_users():
                print("Here is a list of all your Accounts")
                print("\n")
                # for user in display_users():
                user = User.display_user()
                print("\033[1;37;1m  \n")
                print(f"Site: {user.account} \n User Name: {user.username} \n Password: {user.password}")
                    # print(user)
            else:
                print("\033[1;32;1m  \n")
                print(" ")
                print("You don't seem to have any accounts created yet")
if __name__ == '__main__':
	main()
