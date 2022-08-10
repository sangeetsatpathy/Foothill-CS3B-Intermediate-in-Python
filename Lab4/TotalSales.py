def run():
	list = []
	print("You will be entering the amount of money made on each day of the week.")
	for i in range(7):
		list.append(float(input(f"Amount of money made on day {i+1}: $")))
	total = 0
	for i in list:
		total += i
	print(f"The total amount of money made this week was: ${total:.2f}")
		