  #################################################
 # CS03B - Spring 2022
 # Assignment 1 - Question 1
 # Student Name: Sangeet Satpathy
 # SID: 20477554
 #################################################
import math
# Foothill College									
# CS 03B - Object Oriented Programming Methodologies in Python
# Question 1             
# Prepared by Viet Trinh 							
# Email: trinhviet@fhda.edu



class Circle:
  # implement your code here
	def __init__(self, x, y, radius):
		self.x = x
		self.y = y
		self.radius = radius

	@property
	def x(self):
		return self._x
	@x.setter
	def x(self, x):
		self._x = x
	@property
	def y(self):
		return self._y
	@y.setter
	def y(self, y):
		self._y = y
	@property
	def radius(self):
		return self._radius
	@radius.setter
	def radius(self, radius):
		self._radius = radius

	def min_x(self):
		return self.x-self.radius
	def max_x(self):
		return self.x + self.radius
	def min_y(self):
		return self.y - self.radius
	def max_y(self):
		return self.y + self.radius
	

	def getArea(self):
		return self.radius*self.radius*math.pi
		
	def getPerimeter(self):
		return 2*self.radius*math.pi

	def containsPoint(self, x, y):
		change_x_squared = abs(self.x-x)**2
		change_y_squared = abs(self.y-y)**2
		distance = math.sqrt(change_x_squared+change_y_squared)
		if distance > self.radius:
			return False
		return True

	def containsCircle(self, circle):
		a = self.max_x() > circle.max_x()
		b = self.min_x() < circle.min_x()
		c = self.max_y() > circle.max_y()
		d = self.min_y() < circle.min_y()
		if a and b and c and d:
			return True
		return False

	def overlaps(self, circle):
		change_x_squared = abs(self.x-circle.x)**2
		change_y_squared = abs(self.y-circle.y)**2
		distance = math.sqrt(change_x_squared+change_y_squared)
		sum_radii = self.radius + circle.radius
		if sum_radii > distance:
			return True
		return False
	
def run():
	print("===== Question 1 =====")
  	# implement your code here
	circle_1 = Circle(1, 2, 10)
	circle_2 = Circle(2,3,4)
	circle_3 = Circle(-2, 0, 5)
	circle_4 = Circle(0, -3, 6)

	print("Circle 1 Area: " + str(circle_1.getArea()))
	print("Circle 2 Area: " + str(circle_2.getArea()))
	print("Circle 3 Area: " + str(circle_3.getArea()))	
	print("Circle 4 Area: " + str(circle_4.getArea()))

	print("Circle 1 Perimeter: " + str(circle_1.getPerimeter()))
	print("Circle 2 Perimeter: " + str(circle_2.getPerimeter()))
	print("Circle 3 Perimeter: " + str(circle_3.getPerimeter()))
	print("Circle 4 Perimeter: " + str(circle_4.getPerimeter()))

	print(f"Circle 1 contains Point 5,5: {circle_1.containsPoint(5,5)}")
	print(f"Circle 2 contains Point 5,5: {circle_2.containsPoint(5,5)}")
	print(f"Circle 3 contains Point 5,5: {circle_3.containsPoint(5,5)}")
	print(f"Circle 4 contains Point 5,5: {circle_4.containsPoint(5,5)}")

	#What enter numbers for containsCircle
	print("Check if a circle contains another circle")
	bigger_circle = int(input("Which circle are you checking for containing another?: "))
	smaller_circle = int(input("Which circle are you checking for being contained within?: "))
	if bigger_circle == 1:
		if smaller_circle == 2:
			print(circle_1.containsCircle(circle_2))
		elif smaller_circle == 3:
			print(circle_1.containsCircle(circle_3))
		elif smaller_circle == 4:
			print(circle_1.containsCircle(circle_4))
	elif bigger_circle == 2:
		if smaller_circle == 1:
			print(circle_2.containsCircle(circle_1))
		elif smaller_circle == 3:
			print(circle_2.containsCircle(circle_3))
		elif smaller_circle == 4:
			print(circle_2.containsCircle(circle_4))
	elif bigger_circle == 3:
			if smaller_circle == 1:
				print(circle_3.containsCircle(circle_1))
			elif smaller_circle == 2:
				print(circle_3.containsCircle(circle_2))
			elif smaller_circle == 4:
				print(circle_3.containsCircle(circle_4))
	elif bigger_circle == 4:
		if smaller_circle == 1:
			print(circle_4.containsCircle(circle_1))
		elif smaller_circle == 2:
			print(circle_4.containsCircle(circle_2))
		elif smaller_circle == 3:
			print(circle_4.containsCircle(circle_3))


	#Overlap check
	print("Check if two circles overlap each other: ")
	first_circ = int(input("First Circle: "))
	second_circ = int(input("Second Circle: "))

	if first_circ == 1:
		if second_circ == 2:
			print(circle_1.overlaps(circle_2))
		elif second_circ == 3:
			print(circle_1.overlaps(circle_3))
		elif second_circ == 4:
			print(circle_1.overlaps(circle_4))
	elif first_circ == 2:
		if second_circ == 3:
			print(circle_2.overlaps(circle_3))
		elif second_circ == 4:
			print(circle_2.overlaps(circle_4))
	elif first_circ == 3:
		print(circle_3.overlaps(circle_4))
	