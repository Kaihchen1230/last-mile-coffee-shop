# Main Menu
# ONLY WHAT'S ON THE MENU

from application import Application


class Main_Menu:
    """
        Menu object should have the following properties:
            - Account object

    """

    def __init__(self):
        self.app = Application()
        self.options = {

            "1": self.app.add_user,

            "2": self.app.update_user,

            "3": self.app.show_user,

            "4": self.app.delete_user,

            "5": self.app.sign_in
        }

    def display_options(self):
        print(""" 
            ************* MAIN MENU *************
             Welcome to Last Mile Coffee Shop! 

             Please choose one of the options below:
 
             1. Create an account
 
             2. Update account information(s)
 
             3. View current account(s)

             4. Delete account(s)

             Q. Quit

             *************************************

             5. Sign in to your account

             *************************************

 
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
