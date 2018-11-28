colours = ['red', 'blue', 'green', 'yellow', 'purple', 'pink']

def printcolour(index):
	if index == 1:
		number =  "1st"
	elif index == 2:
		number = "2nd"
	elif index == 3:
		number = "3rd"
	else: 
		number = str(index)+"th"
		
	print "The %s colour is at %d and is %s." % (number, index-1, colours[index-1])
	print "The colour at %d is the %s colour and is %s." % (index-1, number, colours[index-1])
	
for i in range(1, 7):
	printcolour(i)