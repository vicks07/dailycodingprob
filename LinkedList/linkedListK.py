class Node:
	def __init__(self,data,nextNode=None):
		self.data = data
		self.next = nextNode

class LinkedList:
	def __init__(self,head=None):
		self.head = head
		self.size = 0
		self.counter = 0

	def addNode(self,data):
		newNode = Node(data,self.head)
		self.head = newNode
		self.size+=1

	def printNode(self,val):
		if val > self.size:
			return "Error"
		currK = self.head		
		curr = self.head
		while curr:				
			if self.counter >= val:
				currK = currK.next			
			curr = curr.next			
			self.counter+=1
		return currK.data

myList = LinkedList()
myList.addNode(5)
myList.addNode(15)
myList.addNode(25)
myList.addNode(30)
myList.addNode(35)
myList.addNode(40)
myList.addNode(45)
myList.addNode(50)
print(myList.printNode(10))