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
        self.app.load() #gets called from application.py
        self.options = {

            "1": self.app.create_account,

            "2": self.app.update_account,

            "3": self.app.search_account,

            "4": self.app.delete_account,

            "5": self.app.sign_in
        }

    def display_options(self):
        print(""" 
            ************* MAIN MENU *************
             Welcome to Last Mile Coffee Shop! 

             Please choose one of the options below:
 
             1. Create an account
 
             2. Update account username

             3. Search for account

             4. Delete account(s)

             5. Sign in to your account

             Q. Quit

             """)

    def run(self):
        while True:
            self.display_options()

            option = input("Enter an option: ")
            if option.lower() == "q":
                print("Now saved all of the data to file")
                self.app.save()
                break

            action = self.options.get(option)

            if action:
                action()
            else:
                print("{0} is not a valid option, please try again!".format(option))
