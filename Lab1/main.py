import random

print("Full name: Sangeet Satpathy")
print("Student ID: 20477554")
print("Email: sangeet.satpathy@gmail.com")
print("Policy 1: Each Student is responsible for dropping out of the class themselves. Simply being absent results in an F.")
print("Policy 2: Late submissions result in a 15% penalty per week")
print("Policy 3: Regrade requests can only be made up till one week after the assignment was graded.")

class Card:
	def __init__(self, suit, val):
		self.suit = suit
		self.value = val

class Deck:
	possible_values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
	possible_suits = ["Hearts","Diamonds","Clubs","Spades"]
	full_deck = []
	current_deck = []
	#Card(possible_suits[i],possible_values[k]) for i<4 or k<13
	
	def __init__(self):
		self.shuffle()
	
	def shuffle(self):
		#Adds all the card values to full_deck list
		for i in range(len(self.possible_values)):
			for k in range(len(self.possible_suits)):
				self.full_deck.append(Card(self.possible_suits[k]),self.possible_values[i])

		#Pulls a random card from the full_deck list, removing it from the full_deck list to ensure it cannot be used again
		while len(self.full_deck) != 0:
			temp = random.choice(self.full_deck)
			self.current_deck.append(temp)
			self.full_deck.remove(temp)

	def deal(self):
		card_to_deal = self.current_deck[0]
		self.current_deck.remove(card_to_deal)
		return card_to_deal
		