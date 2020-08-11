# Class on the user information
class Account:

    """
        Account object should have the following properties:
            - username: string
            - balance: float
            - shpping_cart: list, inside of list should store the item info(would be a good idea to use tuple.
               tuple is this format: (x,y,z)
                    - x: item name
                    - y: item count
                    - z: current item price: item count * the price of the item

        Account object should have the following methods:
            - add_balance(): to update the balance
                - ask the user to enter the amount_of_money that user wants to add
                - the amount_of_money cannot be negative and should be float type (should be a good idea to use try/execpt here)
                - update the balance property by adding the amount_of_money to balance property

            - add_to_shpping_cart(item): add items to shopping_cart
                - item is a tuple format: (item_name, item_count) and passed in from the Sub_Menu object
                - first check if the item_name is in the shopping_cart property
                - if it exist, then simply update the item_count in the shopping_cart property
                - if it doesn't exist, then add it to the shopping_cart property

            - delete_shopping_cart(item_name): delete items from the shopping_cart
                - item_name should be passed in from the Sub_Menu object
                - first check if the item_name is in the shopping_cart property
                - if it does, then delete it from the shopping_cart
                - if it doesn't exist, then display a message for the user, ex: print(f"{item_name} doesn't exist in the shopping cart")

            - display_shopping_cart(): display all of the items within the shopping_cart
                - a for loop to print out each item within shopping_cart property

            - checkout(): calculate the items in the shopping_cart and make sure the balance is enough
                - a for loop to calculate all of the items within shopping_cart property
                - once the calculation for total_price is done, check for the balance property is enough
                - if the balance property is enough, subtract the total_price from the balance and
                  display the new balance to the user and finally empty the shopping_cart property
                - if the balance property is not enough, display a message for user to add more money
    """

    def __init__(self, username, balance):
        self.username = username
        self.balance = balance
        self.shopping_cart = []

    def add_balance(self, amount):

        self.balance += amount
        print(f"Current balance is: ${'% .2f' % self.balance}")

    def add_to_shopping_cart(self, new_item):
        print(new_item)
        (new_item_name, new_item_count, new_item_price) = new_item

        for (item_name, item_count, item_price) in self.shopping_cart:

            if item_name == new_item_name:
                item_count += new_item_count
                item_price += new_item_price
        else:
            self.shopping_cart.append(new_item)

    def remove_from_shopping_cart(self, target_name):

        for i in range(len(self.shopping_cart)):

            item = self.shopping_cart[i]
            item_name = item[0]

            if item_name == target_name:
                self.shopping_cart.pop(i)

        else:
            print(f"{target_name} doesn't exist in your shopping cart.")

    def display_shopping_cart(self):

        total_price = 0
        for (item_name, item_count, item_price) in self.shopping_cart:

            print(f"item name: {item_name}")
            print(f"item count: {item_count}")
            print(f"item total price: {item_price}")
            total_price += item_price

        print("__________________________________________________________")
        print(f"total price: ${total_price}")

    def checkout(self):

        total_price = 0
        for (item_name, item_count, item_price) in self.shopping_cart:

            total_price += item_price

        if total_price <= self.balance:
            self.balance -= total_price
            self.shopping_cart = []
            print("Enjoy your food and drink :)")
            print(
                f"Your current balance in the account: ${'% .2f' % self.balance}")

        else:
            print(
                f"Sorry, your current balance on the account is: ${'% .2f' % self.balance}. You don't have enough of money on your account to pay for your order. Please add money to your account. Thanks.")
