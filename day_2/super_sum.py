def super_sum(A):
	'''
	takes in a list A,and:
	 -halves every even number
	 -doubles every odd number
	and returns the sum of all.
	'''

	total = 0

	for i in A:
		if i % 2 == 0:
			total += (i / 2)
		else:
			total += (i * 2)

	return total



