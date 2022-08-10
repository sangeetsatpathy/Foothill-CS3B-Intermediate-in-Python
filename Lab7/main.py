#Sangeet Satpathy, Lab 7
#Challenge 2
spells = ["protego", "accio", "expecto patronum", "legilimens"]
occurrence = [1, 0, 2, 1]

spells = list(map(lambda x: (x+"!!!"),spells)) 
#Adds the exclamation points to the end of each spell

#This block of code below is to multiply specific spells several times in accordance to occurrence list
multiplied_list = ["" for i in spells]
for i in range(len(spells)):
	for times in range(occurrence[i]):
		if times != 0:
			multiplied_list[i] += " "
		multiplied_list[i] += spells[i]

spells = multiplied_list
print(spells)