def funky(a , b):
	try:
		if type(a) and type(b) == int or float:
			return(a + b)
		if type(a) and type(b) == list:
			return(a + b)
		if type(a) and type(b) == str:
			return(a + b)
	except TypeError as e:
		e = funky
		return 'operand not supported'


