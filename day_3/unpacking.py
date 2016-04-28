def super_sum(a, b, *args):#works with tupples
	'''
	#takes in avariable number of items and returns the sum.
	#e.g. super_sum(20,30,40)=90
	'''
	#set total to 0
	total = 0

	#initialize for loop
	for i in args:

       #add each item to the total
		total += i

	return total + a + b

test values
print super_sum(10,20)
print super_sum(1,4,5,7)
a = [10,40,60]
print super_sum(*a)



def hello_again(**kwargs):#works with dicts

    return "I am {}, and i am {}".format(kwargs['name'], kwargs['age'])

print hello_again(name='joe', age=20)

#other_people = [{'name':'joe', 'age':98},
                # {'name':'jane', 'age':60},]

joe ={'name':'joe', 'age':98}
print hello_again(**joe)
print hello_again(name='joe',age=98)
