from BankAccount import BankAccount
class SavingsAccount(BankAccount):
	annual_rate = 0.06
	#this savings will be compounded monthly at an annual interest rate of 6%
	def __init__(self, username, pin):
		super().__init__(username, pin)

	def month_passed(self,pin):
		if pin != self.pin:
			print("Enter the correct PIN, try again.")
		monthly_interest = 1 + (self.annual_rate/12)
		monthly_return = self.balance*monthly_interest
		amount_added = monthly_return-self.balance
		print(f"This month, you gained ${amount_added:.2f} dollars in your savings account!")
		return amount_added
		
	