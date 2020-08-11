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
        self.accountDict={}

    def create_account(self):
        username= input("Please enter your username: ")
        if username not in self.accountDict.keys():
            try:   
                balance= float(input("How much balance do you want to add to your account?: "))
                if balance >= 0:
                    account = self.Account(username, balance)
                    self.accountDict[username]=account
                    print("Congratulations, you've successfully created your account!")
                else:
                    print("Please enter a amount greater than or equal to $0")
            except ValueError:
                print("Please enter a valid number!")
        else:
            print("That account already exists! Please enter a new username.")


    def search_account(self):
        if self.accountDict={}:
            print("There are no accounts in the application to search!")
        else:
            username= input("Please enter your username you're searching for: ")
            if username in self.accountDict.keys():
                opened_acc=self.accountDict[username]
                print(f"The account {username} currently has $" + opened_acc.balance + " in balance.")
            else:
                print(f"The account with username "{username}" does not exist!")

    def update_account(self):
        if self.accountDict={}:
            print("There are no accounts in the application to update!")
        else:
            username= input("Please enter your username you're updating: ")
            if username in self.accountDict.keys():
                opened_acc=self.accountDict[username]
                new_username= input("Please enter the new username for that account")
                

                print(f"The account {username} currently has $" + opened_acc.balance + " in balance.")
            else:
                print(f"The account with username "{username}" does not exist!")









        if self.userList == {}:
            print("There are no accounts to update!")
        else:
            username = str(input(f"Please enter your username to update: "))
        try:
            if username not in accountDict.keys():
                print("That user does not exist")
            else:
                user_name = str(input("What is the new account username? : "))
                Money= float(input("What is the new amount of money in the account? : "))
                self.userDict[username]=Users_C(user_name,Prin,acc_id)
                return print(f"Your updated username is : \"{user_name}\"") 
        except ValueError:
            print("Please enter a valid number!")

   
    def delete_account(self):
        if self.userList== []:
        print("There are no more accounts to delete!")
        else: 
        user_id = int(input(f"Enter the ID of the user to delete: \n")) ##Add test here
        if(user_id > len(self.userList)):
            print('Please enter a valid user ID!')
        else:
            user_id = user_id - 1
            self.userList.pop(user_id)
            print(f"User Deleted!")
            self.show_user()    

    def login(self):
        username=input("Please enter your username to log in")
        
        
        
        with open('list_of_users.json', 'w') as output_file:
            new =json.dumps(user_List,default=lambda o: o.__dict__, sort_keys=True, indent= 4)
            json.dump(new,output_file)
        
  def quit(self):
    list_of_users = self.userList
    choice = input("Would you like to save all changes (y/n): ")
    if choice == 'y' or choice== 'Y':
      self.save(list_of_users)
    sys.exit(0)



