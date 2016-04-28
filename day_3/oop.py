from person import Person
from kenya import Kenyan





 #p = Person('joe',23)
p2 = Person("jane",34)
p3 = Person("george",100)

 #print p.say_hello()

a = [('jane',23), ('joe',24),('jackie',56),('jee',90),('mena',56)]
b = []
for name, age in a:
	person = Person(name, age)
	b.append(person)
	for i in b:
		print i.say_hello()

print Person.people_count
print p2.people_count #chain lookup,p2 refers to the class to access the function

k = Kenyan('Miguna', 23)
p = Kenyan('joe',23)

k.probe(False)
print "is {} corrupt? {}".format(k.name, k.is_corrupt())

print k.say_hello()
print p.corrupt
print k.corrupt