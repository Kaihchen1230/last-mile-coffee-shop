from account import Account


class Sub_Menu:

    def __init__(self, account):
        self.app = account
        self.price = {'coffee': 1, 'latte': 2, 'cappuccino': 2, 'donut': 1}
        self.options = {

            "1": self.order_menu,

            "2": self.app.add_balance,

            "3": self.app.add_to_shopping_cart,

            "4": self.app.remove_from_shopping_cart,

            "5": self.app.display_shopping_cart,

            "6": self.app.checkout
        }

    def display_options(self):
        print(""" 
            ************* LMTD Coffee Shop *************

             You have successfully signed in! 

             Please choose one of the options below:

             1. View our menu
 
             2. Add balance to your account
 
             3. Add order(s) to your shopping cart
 
             4. Remove order(s) from your shopping cart

             5. Display your current shopping cart

             6. Check out from the store

             Q. Quit

             """)

    def run(self):
        while True:
            self.display_options()
            option = input("Enter an option: ")

            if option == "Q":

                break

            if option == "1":

                self.order_menu()
                continue

            action = self.options.get(option)
            if action:
                action(self.price)

            else:
                print(
                    "{0} is not a valid option, Please try again".format(option))

    def order_menu(self):
        print("""
            Coffee $1
            Latte $2
            Cappuccino $2
            Donut $1
            """)
