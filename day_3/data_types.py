def data_type(x):
	'''
	takes in an argument, x:
	-for an integer, return x ** 2
	-for a float, return x/2
	-for a string, return "hello" + x
	-for a boolean, return "boolean"
	-for a long, return squareroot(x)
	'''
#cheking for integers
	if type(x) == int:
		return x ** 2

#checking for float
	elif type(x) == float:
		return x / 2

#checking for string
	elif type(x) == str:
		return "Hello {}".format(x)

#checking for boolean
	elif type(x) == bool:
		return "boolean"

#checking for long
	elif type(x) == long:
		return "long"

#output for non_data types
	else:
		return "Invalid input:not a data type"

#test
print data_type(50)
print data_type(23.456123456)
print data_type("dad")
print data_type(False)
print data_type(20 ** 20)
print data_type([23,45,50])
