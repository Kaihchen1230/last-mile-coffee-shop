from account import Account


class Sub_Menu:

    def __init__(self, account):
        self.account = account
        self.price = {'coffee': 1, 'latte': 2, 'cappuccino': 2, 'donut': 1}
        self.options = {


            "1": self.add_balance,

            "2": self.add_to_shopping_cart,

            "3": self.remove_from_shopping_cart,

            "4": self.account.display_shopping_cart,

            "5": self.account.checkout
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

    def order_menu(self):
        print("""
            Coffee ----------------------------------  $1
            Latte  ----------------------------------  $2
            Cappuccino ------------------------------  $2
            Donut  ----------------------------------  $1
            """)

    def run(self):
        while True:
            self.display_options()
            self.order_menu()

            option = input("Enter an option: ")

            if option.lower() == "q":
                break

            action = self.options.get(option)
            if action:
                action()

            else:
                print(
                    "{0} is not a valid option, Please try again".format(option))

    def add_balance(self):

        try:
            amount = float(
                input("Enter the amount of money you want to add: "))

            if amount < 0:
                raise Exception("Cannot accept negative value")

            self.account.add_balance(amount)

        except Exception as NegativeAmountError:
            print(NegativeAmountError)

        except:
            print("Only number is allowed!")

    def add_to_shopping_cart(self):

        item_name = input("Enter the name of the item: ").lower()

        if item_name in self.price.keys():

            try:
                item_amount = int(
                    input(f"How many of {item_name} do you want: "))

                item_total_price = self.price[item_name] * item_amount

                self.account.add_to_shopping_cart(
                    (item_name, item_amount, item_total_price))

            except ValueError:
                print("Only number is allowed!")

        else:
            print(f"\"{item_name}\" not in the list")

    def remove_from_shopping_cart(self):

        target_name = input("Enter the name of the item: ").lower()
        self.account.remove_from_shopping_cart(target_name)
