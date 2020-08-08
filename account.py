#Class on the user information
class Users_C:
  def __init__(self, user_name, initial_investment, ID_num):
    self.user_name = user_name
    self.initial_investment = initial_investment
    self.ID_num = ID_num
    self.cash=initial_investment
    self.port={}
    self.net_worth = initial_investment
  def __str__(self):
    return (f"Username: \"{self.user_name}\" | UserID:#{self.ID_num} | Initial Investment Value: $" + f"{self.initial_investment:,.2f}") 
