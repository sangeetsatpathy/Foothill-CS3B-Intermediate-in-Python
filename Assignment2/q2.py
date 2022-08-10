#################################################
 # CS03B - Fall 2020
 # Assignment 2 - Question 2
 # Student Name: Sangeet Satpathy
 # SID: 20477554
 #################################################

# Foothill College									
# CS 03B - Object Oriented Programming Methodologies in Python
# Question 2           
# Prepared by Viet Trinh 							
# Email: trinhviet@fhda.edu
def match_key_value_pairs(dict_1, dict_2):
	null = True
	for i in dict_1: #Iterates through all combinations of dict1 and dict2, checking if they are equal
		for k in dict_2:
			if i==k:#If the keys are the same
				if dict_1[i]==dict_2[k]:#If both the keys and the values are the same:
					print(f"{i}:{dict_1[i]} is present in both these dictionaries.")
					null=False #This is when there is at least one value is present in both dicts.
	if null == True: #If no values are shared, then null will never be turned False, and will print this:
		print("These dictionaries do not share any key:value pairs.")


def sort_counter(dict):
	list_order = [] #List of all the keys in the dict
	for e in dict:
		list_order.append(e)#Append each key in dictionary to list

	for k in range(len(list_order)): #Bubble sort the list_order
		for i in range(len(list_order)):
			if i==0:
				continue
			if dict[list_order[i]] < dict[list_order[i-1]]:
				temp = list_order[i]
				list_order[i]=list_order[i-1]
				list_order[i-1] = temp
			
	sorted_list = [(list_order[n], dict[list_order[n]]) for n in range(len(list_order))] #Once we have the list of all the keys in the dict, we make a list of all the keys and their values in a tuple, such that it is sorted
	print(sorted_list)

def run():
	print("===== Question 2 =====")
  # implement your code here
	print("---Part A----")
	a_dict1 = {'key1': 1, 'key2': 3, 'key3': 2}
	a_dict2 = {'key1': 1, 'key2': 2}
	match_key_value_pairs(a_dict1,a_dict2)
	
	print("---Part B----")
	b_input = {'Math':81, 'Physics':83, 'Chemistry':87} 
	sort_counter(b_input)

	