# Class on the user information
class Account:

    """
        Account object should have the following properties:
            - username: string
            - balance: float
            - shpping_cart: list

        Account object should have the following methods:
            - add_balance: to update the balance
            - update_shpping_cart: add items to shopping_cart
            - delete_shopping_cart: delete items from the shopping_cart
            - checkout: calculate the items in the shopping_cart and make sure the balance is enough
    """

    def __init__(self):
        self.username=username
        self.totalBalance=0
        self.shopping_cart=[]
    
    def add(self):
        username = input(str(f"What is the name of the user? : "))
        add_balance = input(float(f"How much money you want to add?\n"))
        balance = self.totalBalance
        print(f"Your balance is added.#{balance}")
        self.totalBalance +=1
        self.userList.append(user_input)
        print("\nYour username is \""+ str(username) + "\" and your balance is \"" + float(totalBalance)
        

    def update(self):
        if self.shopping_cart== []:
            print("Your shopping cart is empty!")
        else:
            shelf_num = input(f"Which shelf is the book located in?\n")
        try:

        if int(shelf_num) > len(self.bookList):
          print("That shelf is empty. Please try again!")
        else:
          book_name = input(str(f"What is the name of the new book you want to update?\n"))
          self.bookList[int(shelf_num)-1]=Book(book_name,shelf_num)
          return print(f"Your new book is updated!")  
      except ValueError:
        print("Please enter a valid number!")

    def delete(self):
        if self.bookList== []:
      print("The library is empty!")
    else:
      shelf_num = input(f"Which shelf number is the book located on?\n")
      try:
        if int(shelf_num)>len(self.bookList):
          print("That shelf is empty. Please try again!")
        else:
          shelf=int(shelf_num)-1
          self.bookList.pop(shelf)
          print("Book deleted!")
      except ValueError:
        print("Please enter a valid number!")
