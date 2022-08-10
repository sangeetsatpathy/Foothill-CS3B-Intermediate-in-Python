#################################################
 # CS03B - Fall 2020
 # Assignment 2 - Question 3
 # Student Name: Sangeet Satpathy
 # SID: 20477554
 #################################################

# Foothill College									
# CS 03B - Object Oriented Programming Methodologies in Python
# Question 3           
# Prepared by Viet Trinh 							
# Email: trinhviet@fhda.edu

def reverse_string(str):#Reverses a string
	word_list = []
	current_word = ""
	for c in str: #Separates a string into a list of words
		if c==" ":#If there is a space, it means that a new word is starting, add the current word to the list of words and reset current_word
			word_list.append(current_word)
			current_word = ""
			continue
		current_word+=c #If there is no space, keep adding the characters to the current word being formed
	word_list.append(current_word)#Last word, since there is no space at the end
	
	reverse_string = ""
	for word in word_list: #In every word of the word list, reverse it
		i = len(word)-1
		while i>=0:#Starts at the end of each word and adds it to the reverse string, preserving order of the words, but reversing the individual words.
			reverse_string+=word[i]
			i-=1
		reverse_string+=" " #add a space inbetween each word
	print(reverse_string)

def run():
	print("===== Question 3 =====")
  # implement your code here
	reverse_string("Let's take LeetCode contest")
  
