def hello(name, age, class_ = ''):
	'''
	explains...
	'''
	if class_ != '':
		return "I am {}, and I am {} old, and {} class_". format(name, age, class_)

     
	return "I am {}, and I am {} old". format(name, age)

people = [("jane", 23, 'high'),
           ("joe",25, 'middle'),
           ("Brian",60),
           ("betty",45)
           ]

#for name,age in people:
#	print hello(name,age)

	#using unpacking
for person in people:
	print hello(*person)