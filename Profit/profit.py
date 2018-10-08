def minVal(stockPrice):
	low = stockPrice[0]
	index = 0
	for i in range(1,len(stockPrice)):
		if stockPrice[i]<low:
			low = stockPrice[i]
			index = i
		else:
			pass
	return low,index
def maxProfit(stockPrice):
	mVal,index = minVal(stockPrice)
	if index == len(stockPrice)-1:
		return False
	else:
		return mVal,maxValue(stockPrice,index,mVal)

def maxValue(stockPrice,index,val):	
	for i in range(index,len(stockPrice)):
		if stockPrice[i]>val:
			val = stockPrice[i]		
	return val


stockPrice = [9, 11, 8, 7, 10,12]
#print(maxValue(stockPrice,3,5))
print (maxProfit(stockPrice))