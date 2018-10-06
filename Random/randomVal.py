import random
def rand7():
	val = (rand5()+rand5())%8
	return val if val > 1 else val+1

def rand5():
	return random.randint(1,5)

print (rand7())