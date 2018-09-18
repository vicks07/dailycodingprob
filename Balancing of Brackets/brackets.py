class Stack:
	def __init__(self):
		self.stack = []

	def add(self,data):
		self.stack.append(data)
		return True
	
	def remove(self):
		return self.stack.pop()

	def CheckBalance(self,data):
		for val in data:
			#print (val)
			if val == '(' or val == '[' or val =='{':
				brackets.add(val)
			elif len(self.stack)==0:
				return False
			elif val == ')' or val == ']' or val =='}':
				temp = brackets.remove()
				#print (temp)
				if temp == '(' and (val=='}' or val ==']'):
					return	False
				elif temp =='[' and (val=='}' or val ==')'):
					return	False
				elif temp =='{' and (val==']' or val ==')'):
					return	False
		if(len(self.stack) > 0):
			return False
		else:
			return True


brackets = Stack()
data = "((()"#"([])[]({})"#"([)]"
#rackets.add("([)]","")



#print (brackets.stack)
print (brackets.CheckBalance(data))


