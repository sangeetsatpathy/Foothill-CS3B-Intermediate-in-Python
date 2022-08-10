class Organism:
	def __init__(self, species):
		self.name = species

	def make_energy(self):
		print("Different organisms have different means of making energy.")

	def introduction(self):
		print(f"I am an Organism")

class Plant(Organism):
	def __init__(self, species):
		Organism.__init__(self, species)
	def make_energy(self):
		print("Plants make energy through photosynthesis")

o = Organism("Random Organism")
p = Plant("Poison oak")

o.make_energy() #"Different organisms have different means of making energy"
o.introduction() #"I am an Organism"

p.make_energy()#"Plants make energy through photosynthesis"
#Plant make_energy method has same signature as Organism, but we use the subclass method, since there is one.

p.introduction()#"I am an Organism"
#Since there is no introduction method in the Plant class, it refers to the superclass, where it finds the method.
