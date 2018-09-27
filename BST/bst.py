class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	def insert(self,data):
		if self.data:
			if self.data > data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif self.data < data:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
			else:
				self.data = data
	

	def Largest(self,root):		
		if root.data:
			if root.right is None:
				return (root.data)
			else:
				root.Largest(root.right)

	def secondLargest(self):
		current = self		
		while current:
			if current.left and not current.right: #If the current node is the largest, get the largest from the left subtree
				return self.Largest(current.left)
			if current.right and not current.right.left and not current.right.right:
				return current.data
			current = current.right
		

root = Node(12)
root.insert(6)
root.insert(10)
root.insert(14)
root.insert(20)
root.insert(18)

print(root.secondLargest())
