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
    def find_user(account):
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
