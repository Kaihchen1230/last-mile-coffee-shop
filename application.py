#CRUD for Main Menu
#ex.

from Users import Users_C
from Search_Stocks import search_stock
import sys
import json
import os

class Application:
      
  def __init__(self):
    self.ID=1
    self.userList=[] #dictionary of accounts (connects with portfolio)

  def add_user(self):
    account_name = input(str(f"What is the name of the user? : "))
    ID = self.ID
    invest_amount = float(input("What amount would you like to start investing? : "))
    user_input = Users_C(account_name, invest_amount, ID)
    self.userList.append(user_input)
    print("\nAccount created!\nYour username is \""+ str(account_name) + "\" and your personal user id is \"" + str(ID) + "\"")
    self.ID +=1

  def update_user(self):
    if self.userList == []:
      print("There are no accounts to update!")
    else:
      acc_id = int(input(f"Please enter the ID of the account to update: "))
      try:
        if int(acc_id)> len(self.userList):
          print("That user does not exist")
        else:
          user_name = str(input("What is the new account username? : "))
          Prin= float(input("What is the new invesment amount in the account? : "))
          self.userList[int(acc_id)-1]=Users_C(user_name,Prin,acc_id)
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



  def sign_in(self):
    if self.userList== []:
      print("There are no users in the application!")
    else:
      User_ID= int(input("Please enter your user ID to log in: "))
      if User_ID > len(self.userList):
        print('That user ID does not exist!')
      else:
        opened_acc=self.userList[int(User_ID)-1]
        print("\nWelcome "+ opened_acc.user_name + '!') 
        print("""
        Choose from the options below
        "1": Search stock
        "2": Buy Stock
        "3": Sell Stock
        "4": Check Portfolio
        "5": Return to menu
              """)
        x = int(input("enter: "))

        if x==1:
          self.search_stock(opened_acc)
          return(self.sign_in())
        elif x==2:
          self.buy_stock(opened_acc)
          return(self.sign_in())
        elif x==3:
          self.sell_stock(opened_acc)
          return(self.sign_in())
        elif x ==4:
          self.check_portfolio(opened_acc)
          return(self.sign_in())
        else:
          return

  def search_stock(self,user):
    stock_symbol = input("Please enter the Stock Ticker: ")
    try:
      search_stock(stock_symbol)
    except KeyError:
      print("That stock does not exist. Please enter a valid stock ticker!\n")
      return

  def buy_stock(self,user):
    print("You currently have $" +str(user.cash)+ " available to spend in your account")
    stock_symbol = input("Please enter the Stock Ticker: ")
    try:
      stock= search_stock(stock_symbol)
    except KeyError:
      print("That stock does not exist. Please enter a valid stock ticker!\n")
      return
    stock_price=stock.value #price got from search_stock class
    quant= int(input("How many of this stock would you like to purchase? : "))
    if (quant*stock_price) > user.cash:
      print('You do not have enough cash to complete your purchase.')
    else:
      user.cash=user.cash - (quant*stock_price)
      user.port[stock_symbol]=[quant,stock_price] #Stores it to portfolio dictionary
      if quant == 1:
        print('You now have '+ str(quant) + ' share of ' +str(stock_symbol).upper() + " and $" + str(user.cash)+ " in cash left in your account\n")
      else:
        print('You now have '+ str(quant) + ' shares of ' +str(stock_symbol).upper() + " and $" + str(user.cash)+ " in cash left in your account!\n")
    
  def sell_stock(self, user):
    print("This is your current portfolio: ")
    for key in user.port:
      if user.port[key][0] > 1:
        print(str(user.port[key][0]) + " shares of " + key.upper() +  " worth " + str(user.port[key][1]) +" each.")
      else:
        print(str(user.port[key][0]) + " share of " + key.upper() +  " worth " + str(user.port[key][1]) +" each.")
    stock= input("\nWhich stock would you like to sell? ")
    if stock in user.port:
      quant=int(input("How many of those shares would you like to sell? "))
      if quant > user.port[stock][0] or quant <0:
        print("You can only sell" + user.port[stock][0])
      else:
        new= user.port[stock][0] - quant
        user.port[stock][0]= new
        surplus= user.port[stock][1]*quant
        user.cash=user.cash + surplus
        if quant==1:
          print("You have now sold " + str(quant) + " share of " + stock.upper() + " and" + " $" + str(surplus)+ " has been added to your account")
        else:
          print("You have now sold " + str(quant) + " shares of " + stock.upper() + " and" + " $" + str(surplus)+ " has been added to your account")
    else:
      print("You do not own that stock!")




  def check_portfolio(self, user):
    print(f"\nInitial investment ${user.initial_investment}")
    print (f"Current cash in the account: $" + str(round(user.cash, 2)))
    print("________________________________")
    if len(user.port) ==0 :
      print("There are no stock investments currently in the portfolio.\n")
    else:
      print(f"Account's stock portfolio: ")
      for key in user.port:
        if user.port[key][0] > 1:
          print(str(user.port[key][0]) + " shares of " + key.upper() +  " worth " + str(user.port[key][1]) +" each.")
        else:
          print(str(user.port[key][0]) + " share of " + key.upper() +  " worth " + str(user.port[key][1]) +" each.")
      print('\n')


  def changes(self, user):
    changes = user.cash - user.initial_investment / user.initial_investment
    print(f"your initial investment was {user.initial_investment}")
    print(f"your change in accouunt balance is: ")
    print (changes)


