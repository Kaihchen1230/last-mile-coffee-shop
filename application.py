from subMenu import Sub_Menu
from account import Account


class Application:

    def __init__(self):
        self.accountDict={}


    def create_user(self):
        username= input(str("Please enter your username: "))
        money= float(input("How much money do you want to add in your account?: "))
        account = self.Account(username, money)
        self.accountDict.update(account)
        print("Congratulations, you've successfully created your account!")

    def search_user(self):
        username= input(str("Please enter the username you're trying to search"))
        if self.accountDict={} or username in self.accountDict.key:
            print(f"Account found! Your account "{username}" has $" + self.accountDict[username])
        else:
            print("Error, please try again!")

    def update_user(self):
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
      
  def show_user(self):
    if self.userList == []:
      print("There are no accounts to view!")
    else:
      print("""\n___________________________________________________________________\n
               Current accounts in our stock exchange:
      """)
    for user in self.userList:
      print(user)
      print("""___________________________________________________________________
      """)
    return self.userList
   
  def delete_user(self):
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

  def save(self,user_List):
     with open('list_of_users.json', 'w') as output_file:
        new =json.dumps(user_List,default=lambda o: o.__dict__, sort_keys=True, indent= 4)
        json.dump(new,output_file)
        
  def quit(self):
    list_of_users = self.userList
    choice = input("Would you like to save all changes (y/n): ")
    if choice == 'y' or choice== 'Y':
      self.save(list_of_users)
    sys.exit(0)



    """
        Application object should have the following properties:
            - accounts: a list of Account object
            - sub_menu: a Sub_Menu object

        Application object should have the following methods:
            - create_account: create the account and stored it into accounts
            - search_account: search if the account existed in accounts list
            - show_balance: show the balance of the account based on the username
            - delete_account: delete account based on the username
    """

 
