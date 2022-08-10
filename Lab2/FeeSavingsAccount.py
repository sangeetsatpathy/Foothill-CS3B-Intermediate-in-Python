from SavingsAccount import SavingsAccount

class FeeSavingsAccount(SavingsAccount):
	def __init__(self, username, pin, account_fee):
		super().__init__(username, pin)
		self.fee = account_fee
	def withdraw(self, pin, amount):
		if pin != self.pin:
			print("Wrong PIN. Please try again and enter the correct PIN.")
			return

		total_withdraw = amount + self.fee
		
		if total_withdraw>self.balance:
			print("You do not have enough money in your account to withdraw this amount. Try again.")
			return
		self.balance -= total_withdraw
		print(f"Withdrew ${amount:.2f} from your savings account in addition to the fee of ${self.fee:.2f}")
		return total_withdraw