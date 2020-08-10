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

    def __init__(self):
        pass
