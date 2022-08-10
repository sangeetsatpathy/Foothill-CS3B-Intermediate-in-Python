 #################################################
 # CS03B - Spring 2022
 # Assignment 1 - Question 3
 # Student Name: Sangeet Satpathy
 # SID: 20477554
 #################################################
# Foothill College									
# CS 03B - Object Oriented Programming Methodologies in Python
# Question 3           
# Prepared by Viet Trinh 							
# Email: trinhviet@fhda.edu


# Implement your Employee class here
class Employee:
	def __init__(self, name, id):
		self.employee_name = name
		self.employee_number = id

	@property
	def employee_name(self):
		return self._employee_name

	@employee_name.setter
	def employee_name(self, newname):
		self._employee_name = newname

	@property
	def employee_number(self):
		return self._employee_number

	@employee_number.setter
	def employee_number(self, newid):
		self._employee_number = newid
	
	

# Implement your ProductionWorker class here
class ProductionWorker(Employee):
	def __init__(self, name, id, shift_number, pay_rate):
		Employee.__init__(self, name, id)
		self.shift_number = shift_number
		self.pay = pay_rate

	@property
	def shift_number(self):
		return self._shift_number

	@shift_number.setter
	def shift_number(self, new_shift):
		if new_shift == 1 or new_shift == 2:
			self._shift_number = new_shift
		else:
			print("There are only 2 shifts - shift #1 for daytime, shift#2 for nighttime.")

	@property
	def pay(self):
		return self._pay

	@pay.setter
	def pay(self, newpay):
		self._pay = newpay

def run():
	print("===== Question 3 =====")
  # implement your code here
	name = input("Enter employee name: ")
	id = input("Enter Employee ID Number: ")
	shift = 0
	while shift != 1 and shift!=2:
		shift = int(input("Enter a valid shift — Shift 1 for Daytime, Shift 2 for nighttime: "))
	pay = input("Enter Employee Hourly Pay: $")
	worker = ProductionWorker(name, id, shift, pay)
	print(f"Worker's Name: {worker.employee_name}")
	print(f"Worker ID: {worker.employee_number}")
	print(f"Worker Shift: {worker.shift_number}")
	print(f"Worker hourly pay: ${worker.pay}")
