#Sangeet Satpathy
#Lab 9
#CS 3B
#6/5/22
#Challenge 1

#Note: this program doesn't optimize it fully, but I do not know how to fully optimize it to get the smallest amount of numbers.
import math
def leastNumSquares(n):
	remaining = n
	listNums = [i*i for i in range(math.floor(math.sqrt(n)+1))]
	numsUsed = []
	while remaining!=0:
		biggestNum = listNums[-1]
		numberOfTimes = math.floor(remaining/biggestNum)
		for i in range(numberOfTimes):
			numsUsed.append(biggestNum)
		remaining  = remaining % biggestNum
		listNums.pop()
	return numsUsed
print(f"Smallest list that adds to 12: {leastNumSquares(12)}")
print(f"Number of integers added: {len(leastNumSquares(12))}")
	