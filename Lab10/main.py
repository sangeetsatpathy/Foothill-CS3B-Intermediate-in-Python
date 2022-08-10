#Sangeet Satpathy
#Lab 10
#CS 3B
#6/13/22
from LinkedList import *
def rotateList(linkedList, k):
	for i in range(k):
		rotateOnce(linkedList)

def rotateOnce(linkedList):
	beginning = linkedList.head #Points to first node in LinkedList
	pointer = beginning
	if pointer.next.next is None: #Pointer refers to the 2nd to last node
		linkedList.head = pointer.next #Makes the last node into the new head of the SLL
		pointer.next.next = beginning #Sets the new head's next to the old beginner node.
		pointer.next = None # The pointer's next now refers to Null, making it the last node of the SLL now

beginner_node = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
sll = LinkedList(beginner_node)
beginner_node.next = node2
beginner_node.next.next = node3
beginner_node.next.next.next = node4
beginner_node.next.next.next.next = node5
sll.print_sll()
rotateList(sll, 2)
sll.print_sll() #I do not know why the second print is not 
#correctly printing the rotated list. The algorithm should work.