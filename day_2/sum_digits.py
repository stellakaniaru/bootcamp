def sum_digits(A):
	'''
	takes in a list A, and returns the sum 
	of all the digits in the list e.g. [10,30,45] 
	should return 1 + 0 + 3 + 0 + 4 + 5 = 13
	'''
	total=0

	while i:
		total += (i % 10)
        i //= 10
	return total

print sum_digits([400,10,30])


