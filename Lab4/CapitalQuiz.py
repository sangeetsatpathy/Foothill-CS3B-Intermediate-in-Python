import random
def run_quiz():
	capitals_states = {
		"Alabama":"Montgomery",
		"Alaska":"Juneau",
		"Arizona":"Phoenix",
		"Arkansas":"Little Rock",
		"California":"Sacramento",
		"Colorado":"Denver",
		"Connecticut":"Hartford",
		"Delaware":"Dover",
		"Florida":"Tallahassee",
		"Georgia":"Atlanta",
		"Hawaii":"Honolulu",
		"Idaho":"Boise",
		"Illinois":"Springfield",
		"Indiana":"Indianapolis",
		"Iowa":"Des Moines",
		"Kansas":"Topeka",
		"Kentucky":"Frankfort",
		"Louisiana":"Baton Rouge",
		"Maine":"Augusta",
		"Maryland":"Annapolis",
		"Massachusetts":"Boston",
		"Michigan":"Lansing",
		"Minnesota":"Saint Paul",
		"Mississippi":"Jackson",
		"Missouri":"Jefferson City",
		"Montana":"Helena",
		"Nebraska":"Lincoln",
		"Nevada":"Carson City",
		"New Hampshire":"Concord",
		"New Jersey":"Trenton",
		"New Mexico":"Santa Fe",
		"New York":"Albany",
		"North Carolina":"Raleigh",
		"North Dakota":"Bismarck",
		"Ohio":"Columbus",
		"Oklahoma":"Oklahoma City",
		"Oregon":"Salem",
		"Pennsylvania":"Harrisburg",
		"Rhode Island":"Providence",
		"South Carolina":"Columbia",
		"South Dakota":"Pierre",
		"Tennessee":"Nashville",
		"Texas":"Austin",
		"Utah":"Salt Lake City",
		"Vermont":"Montpelier",
		"Virginia":"Richmond",
		"Washington":"Olympia",
		"West Virginia":"Charleston",
		"Wisconsin":"Madison",
		"Wyoming":"Cheyenne"
	}
	print("Quiz of Capitals! You will be given a state, you will have to type the capital of that state!")
	num_questions = 0
	correct_answers = 0
	end = False
	while end == False:
		choice = random.choice(list(capitals_states))
		guess = input(f"What is the capital of {choice}? If you would like to quit instead, type '1': ")
		num_questions += 1
		if guess == capitals_states[choice]:
			correct_answers+=1
			print(f"That is correct! Your current score is {correct_answers}/{num_questions}!")
		else:
			if guess == "1":
				end = True
				print(f"Game ended. Your ending score was {correct_answers}/{num_questions-1}")
			else:
				print(f"Incorrect choice. The answer was {capitals_states[choice]}. Your score is currently {correct_answers}/{num_questions}")
				
			
	