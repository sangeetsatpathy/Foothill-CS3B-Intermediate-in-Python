from BankAccount import BankAccount
from SavingsAccount import SavingsAccount
from FeeSavingsAccount import FeeSavingsAccount

print("BankAccount: ")
my_account = BankAccount("Sangeet",1020)
my_account.get_balance(1020)
my_account.deposit(00000,50)
my_account.deposit(1020,0.3)
my_account.get_balance(1020)
my_account.withdraw(1020, 0.4)

print()
print("Savings Account: ")
my_savings = SavingsAccount("Sangeet",3040)
my_savings.get_balance(3040)
my_savings.deposit(0000, 50)
my_savings.deposit(3040,0.3)
my_savings.deposit(3040,54.33)
my_savings.get_balance(3040)
my_savings.withdraw(3040,0.4)
my_savings.month_passed(3040)
my_savings.get_balance(3040)

print()
print("FeeSavingsAccount: ")
fee_savings = FeeSavingsAccount("Sangeet",5060, 0.1)
fee_savings.get_balance(5060)
fee_savings.deposit(0000, 50)
fee_savings.deposit(5060,0.35)
fee_savings.get_balance(5060)
fee_savings.withdraw(5060,0.3)
fee_savings.withdraw(5060,0.2)