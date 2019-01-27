import pyperclip
from user import User
#To add an account
def create_account(account,username,password):
    '''
    Function to create a new account
    '''
    new_user = User(account,username,password)
    return new_user
