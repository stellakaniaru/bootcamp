class Person(object):
#class variable 
	people_count = 0

	def __init__(self, name, age):
		#instance variable
		self.name = name
		self.age = age
		Person.people_count += 1

	def __repr__(self):
		return "object: {}, {}>".format(self.name, self.age)

	def say_hello(self):
		return "Hello, I am {} and {} y/o".format(self.name, self.age)
class Kenyan(Person):
	corrupt = False

	def probe(self, corrupt):
		self.corrupt = corrupt

	def is_corrupt(self):
		if self.corrupt:
			return "Yes"
		return "No"

k = Kenyan('Miguna', 23)

k.probe(False)
print "is {} corrupt? {}".format(k.name, k.is_corrupt())

print k.say_hello()