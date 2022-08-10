#################################################
 # CS03B - Fall 2020
 # Assignment 2 - Question 4
 # Student Name: Sangeet Satpathy
 # SID: 20477554
 #################################################

# Foothill College									
# CS 03B - Object Oriented Programming Methodologies in Python
# Question 4           
# Prepared by Viet Trinh 							
# Email: trinhviet@fhda.edu

def unpack(list):#Unpacks a list of lists
	unpacked_list=[]
	for i in list:
		for k in i:
			unpacked_list.append(k)
	return unpacked_list

def k_grammar(n, k):
	current_row = []
	for i in range(n):#each row
		if i==0:
			current_row.append(0)
			continue
		for iter in range(len(current_row)):
			if current_row[iter] == 0: #every time there is a 0 in the list, it is replaced with 01 --> did this with a nested list
				current_row[iter]=[0,1]
			elif current_row[iter] == 1:#every time there is a 1 in the list, it is replaced with 10 --> did this with nested list
				current_row[iter]=[1,0]
		#unpacking nested lists
		current_row = unpack(current_row)
	print(current_row[k-1])#k-1 because list indeces start at 0

def run():
	print("===== Question 4 =====")
  # implement your code here
	k_grammar(4, 5)
