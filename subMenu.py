from account import Account


class Sub_Menu:

    def __init__(account):
        self.app = account
        self.options = {

            "1": self.app.add_balance,

            "2": self.app.add_to_shopping_cart,

            "3": self.app.remove_from_shopping_cart,

            "4": self.app.display_shopping_cart,

            "5": self.app.checkout
        }

    def display_options(self):
        print(""" 
            ************* LMTD Coffee Shop *************

             You have successfully signed in! 

             Please choose one of the options below:
 
             1. Add balance to your account
 
             2. Add order(s) to your shopping cart
 
             3. Remove order(s) from your shopping cart

             4. Display your current shopping cart

             5. Check out from the store

             Q. Quit

             """)

    def run(self):
        while True:
            self.display_options()
            option = input("Enter an option: ")
            if option== "Q":
                break
            action = self.options.get(option)

            if action:
                action()
            else:
                print("{0} is not a valid option, Please try again".format(option))


    """
        Sub_Menu object should have the following properties:
            - Account object (passed in from the application)

        Sub_Menu is the frontend for the logged in user
    """

    def __init__(self):
        pass
