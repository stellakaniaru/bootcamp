f = [(10, 20, 40), (10,40), (4, 5, 50)]
'''
x:10, y:20, z:40
x:10, y:40
'''

	
for i in f:
	if len(i) == 3:
		print "x : {}, y : {}, z : {}".format(*i)

	else:
		print "x : {}, y : {}".format(*i)
		