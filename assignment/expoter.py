
people =[
      ('joe',78),('janet',90),('brain', 67)]


def super_sum(*args):
	return sum(args)


def hello_again(name, age):
	return "I am {} and {} years old".format(name, age)

def max_min(A):
	'''
	returns max value - min value
	e.g 
	'''
	#return max(A) - min(A)
	max_, min_ = A[0], A[0]

	for i in A:
		if i > max_:
			max_ = i
		if i < min_:   #try with elif to see what happens
			min_ = i

	return max_ - min_