#Sangeet Satpathy
#CS3B
#Lab 5
#Challenge 2
def pow(base, exponent):
	if exponent == 0:
		return 1
	if exponent == 1:
		return base
	return pow(base, exponent-1)*base

print(pow(4,3))