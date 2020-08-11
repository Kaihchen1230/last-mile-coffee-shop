from subMenu import Sub_Menu
from account import Account


class Application:

    """
        Application object should have the following properties:
            - accounts: a list of Account object
            - sub_menu: a Sub_Menu object

        Application object should have the following methods:
            - create_account():
                - ask user to enter an username
                - ask user to enter amount_of_money to add to the account
                - use the username and amount_of_money to create an Account object
                - add the Account object to the accounts list

            - search_account(): search if the account existed in accounts list
                - ask user to enter an username to search
                - search that username in the accounts list
                - then display the Account object info
                - if it doesn't exist, then print a message for the user 

            - update_account(): update the account username if it existed in the account list
                - ask user to enter an username to be updated
                - search for the username in the accounts list
                - if it existed, ask the user to enter a new username
                - update the username based on user's input
                - if it doesn't exist, then print a message for the user 

            - delete_account(): delete account based on the username
                - ask the user to enter the username
                - search for the username in the accounts list
                - if it existed, delete it from the accounts list
                - if it doesn't exist, then print a message for the user 

            - login():
                - ask the user to enter the username
                - if it existed in the accounts list, then create a Sub_Menu object and pass the Account object associated
                  with the username to the Sub_Menu object
                - invoke the Sub_Menu's run menthod
                - if it doesn't exist, then print a message for the user 
    """

    def __init__(self):
        pass
