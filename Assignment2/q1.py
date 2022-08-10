#################################################
 # CS03B - Fall 2020
 # Assignment 2 - Question 1
 # Student Name: Sangeet Satpathy
 # SID: 20477554
 #################################################

# Foothill College									
# CS 03B - Object Oriented Programming Methodologies in Python
# Question 1           
# Prepared by Viet Trinh 							
# Email: trinhviet@fhda.edu

#Name1 and Name2 are the value names for the first and second list.
def list_to_listofdicts(list1, list2, name1, name2):
	list_of_dicts = [{name1:list1[n],name2:list2[n]} for n in range(len(list1))]#Match the indeces of the first and second lists along with the value names provided.
	return list_of_dicts

def dict_from_2_lists(list1, list2):
	dict = {}
	for i in range(len(list1)):
		dict[list1[i]] = list2[i] #Assign the corresponding indeces in key:value pairs for dictionary.
	return dict
		
def run():
	print("===== Question 1 =====")
  # implement your code here
	print("---Part A----")
	a_list1 = ["Black","Red","Maroon", "Yellow"]
	a_list2 = ["#000000", "#FF0000", "#800000", "#FFFF00"]
	print(list_to_listofdicts(a_list1, a_list2, "color_name","color_code"))
	print("---Part B----")	
	b_list1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
	b_list2 = [1, 2, 2, 3]
	print(dict_from_2_lists(b_list1, b_list2))
