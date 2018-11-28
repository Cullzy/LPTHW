def looped(max, increment):
	numbers = []
	i = 0
	while i < max:
		numbers.append(i)
		print "Item = %d" % i 
		i += increment
		print numbers 

looped(50, 5)