# import unittest
class User :

    """
    Class that generates new instances of users
    """

    user_list = []
    def __init__ (self, account, username, password):

        '''
        __init__ method that helps us define properties for our objects.
        '''

        self.account = account
        self.username = username
        self.password = password
