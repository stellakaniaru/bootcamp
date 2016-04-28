def super_sum(*args):
	'''
	returns a sum of numbers.
	e.g
	   super_sum() ==> "0
	   super_sum('string') ==>
	   super_sum(1, 2, 3) ==> 6
	   super_sum([1, 2, 3]) ==> 6
	   super_sum([10],[20, 30]) ==>60
	   '''
	total = 0
	if not args:
		return 0

	else:
		for x in args:
			if type(x) == list:
				total += sum(x)
			elif type(x) == str:
				return 0
			else:
				total += x

		return total



