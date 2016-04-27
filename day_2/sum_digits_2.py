def sum_digits(A):
	'''
	takes in a list A, and returns the sum 
	of all the digits in the list e.g. [10,30,45] 
	should return 1 + 0 + 3 + 0 + 4 + 5 = 13
	'''
	
	total = 0
	for a in A:
	    B = str(a)
	    for b in B:
		    total += int(b)
	return total

print sum_digits([1006,320])
