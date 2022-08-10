#Lab 6 - Sangeet Satpathy
#Challenge 1

food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
fifth = []
for x in food:
	try:
		fifth.append(x[4])
	except:
		pass

print(fifth)