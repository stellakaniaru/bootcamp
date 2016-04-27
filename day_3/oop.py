class Person:
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

p = Person('joe',23)
p2 = Person("jane",34)
p3 = Person("george",100)

print p.say_hello()

a = [('jane',23), ('joe',24),('jackie',56),('jee',90),('mena',56)]
b = []
for name, age in a:
	person = Person(name, age)
	b.append(person)
	for i in b:
		print i.say_hello()

print Person.people_count
print p2.people_count #chain lookup,p2 refers to the class to access the function