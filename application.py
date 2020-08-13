from subMenu import Sub_Menu
from account import Account
import json
import time


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

            - sign_in():
                - ask the user to enter the username
                - if it existed in the accounts list, then create a Sub_Menu object and pass the Account object associated
                  with the username to the Sub_Menu object
                - invoke the Sub_Menu's run menthod
                - if it doesn't exist, then print a message for the user
    """

    def __init__(self, accountDic={}):
        self.accountDict = accountDic

    def create_account(self):
        username = input("Please enter your username: ")
        if username not in self.accountDict.keys():
            try:
                balance = float(
                    input("How much balance do you want to add to your account?: "))
                if balance >= 0:
                    account = Account(username, balance)
                    self.accountDict[username] = account
                    print(
                        "Congratulations, you've successfully created your account!\n")
                else:
                    print("Please enter a amount greater than or equal to $0\n")
            except ValueError:
                print("Please enter a valid number!\n")
        else:
            print("That account already exists! Please enter a new username.\n")

        time.sleep(2)

    def search_account(self):
        if self.accountDict == {}:
            print("There are no accounts in the application to search!\n")
        else:
            username = input(
                "Please enter your username you're searching for: ")
            if username in self.accountDict.keys():
                opened_acc = self.accountDict[username]
                print(
                    f"The account {username} currently has ${'% .2f' % opened_acc.balance} in balance.\n")
            else:
                print(
                    f"The account with username \"{username}\" does not exist!\n")

        time.sleep(2)

    def update_account(self):
        if self.accountDict == {}:
            print("There are no accounts in the application to update!\n")
        else:
            username = input("Please enter your username you're updating: ")
            if username in self.accountDict.keys():
                new_username = input(
                    "Please enter the new username for that account: ")
                # print(self.accountDict.pop(username))

                update_account = self.accountDict[username]
                update_account.username = new_username

                self.accountDict[new_username] = self.accountDict.pop(username)

                print(
                    f"The username of \"{username}\" has been changed to \"{new_username}\"\n")

            else:
                print(
                    f"The account with username \"{username}\" does not exist!\n")

        time.sleep(2)

    def delete_account(self):
        if self.accountDict == {}:
            print("There are no accounts in the application to delete!\n")
        else:
            username = input("Please enter the username you're deleting: ")
            if username in self.accountDict.keys():
                self.accountDict.pop(username)
                print(
                    f"The account with username \"{username}\" has been successfully deleted!")
            else:
                print(
                    f"The account with username \"{username}\" does not exist!\n")

        time.sleep(2)

    def sign_in(self):
        if self.accountDict == {}:
            print("There are no accounts in the application to sign in to!\n")
        else:
            username = input("Please enter your username to sign in: ")
            if username in self.accountDict.keys():
                account_info = self.accountDict[username]
                signed_In = Sub_Menu(account_info)
                signed_In.run()
            else:
                print(
                    f"The account with username \"{username}\" does not exist!\n")

        time.sleep(2)

    @classmethod
    def from_json(cls, data):

        accounts = list(map(Account.from_json, data))
        decoded_accounts = {}
        for account in accounts:
            # print('account: ', account)
            decoded_accounts[account.username] = account

        return decoded_accounts

    # def display_accounts(self):

    #     for ueranme, account_info in self.accountDict.items():

    #         print('this is ueranme: ', ueranme)
    #         print('this is account_info: ', account_info)

    def load(self):
        with open("accounts.json", "r") as accounts_json:
            data = json.load(accounts_json)
            decoded_accounts = Application.from_json(json.loads(data))
            self.accountDict = decoded_accounts

    def save(self):

        data = json.dumps(list(map(
            lambda username: self.accountDict[username].__dict__, self.accountDict.keys())))

        with open("accounts.json", "w") as accounts_json:

            json.dump(data, accounts_json)


