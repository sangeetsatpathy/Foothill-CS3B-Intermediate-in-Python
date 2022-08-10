 #################################################
 # CS03B - Spring 2022
 # Assignment 1 - Question 2
 # Student Name: Sangeet Satpathy
 # SID: 20477554
 #################################################
import math
# Foothill College									
# CS 03B - Object Oriented Programming Methodologies in Python
# Question 2             
# Prepared by Viet Trinh 							
# Email: trinhviet@fhda.edu

class Triangle:
  # implement your code here
	def __init__(self, side1=1.0, side2=1.0, side3=1.0):
		self.side1 = side1
		self.side2 = side2
		self.side3 = side3

	@property
	def side1(self):
		return self._side1
	@side1.setter
	def side1(self, newval):
		self._side1 = newval
	@property
	def side2(self):
		return self._side2
	@side2.setter
	def side2(self, newval):
		self._side2 = newval
	@property
	def side3(self):
		return self._side3
	@side3.setter
	def side3(self, newval):
		self._side3 = newval

	def getArea(self):
		loc_1 = (self.side2**2)+(self.side3**2)-(self.side1**2)
		loc_2 = 2*self.side2*self.side3
		loc_3 = loc_1/loc_2
		loc_4 = math.acos(loc_3)
		height = self.side2*math.sin(loc_4)
		return self.side3*height/2

	def getPerimeter(self):
		return self.side1+self.side2+self.side3

	def toString(self):
		str_to_return = f"Side 1 Length: {self.side1}. Side 2 Length: {self.side2}. Side 3 Length: {self.side3}."
		return str_to_return

def run():
	print("===== Question 2 =====")
  # implement your code here
	tri_1 = Triangle()
	tri_2 = Triangle(3, 4, 5)
	print(f"Area of first triangle: {tri_1.getArea()}")
	print(f"Area of second triangle: {tri_2.getArea()}")
	print(f"Perimeter of first triangle: {tri_1.getPerimeter()}")
	print(f"Perimeter of second triangle: {tri_2.getPerimeter()}")
	
  