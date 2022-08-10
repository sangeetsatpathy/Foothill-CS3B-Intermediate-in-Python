#Sangeet Satpathy
#Lab 10
#CS 3B
#6/13/22
class Node:
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

	def set_head(self, data):
		self._data = data

	def get_head(self):
		return self._data

	def set_next(self, next):
		self._next = next

	def get_next(self):
		return self._next

class LinkedList:
	def __init__(self, head=None): #Head is the first node
		self.head = head

	def set_head(self, head):
		self._head = head

	def get_head(self, head):
		return self._head
	def print_sll(self):
		pointer = self.head
		while pointer is not None:
			print(pointer.data, end = ' ')
			pointer = pointer.next
		print()