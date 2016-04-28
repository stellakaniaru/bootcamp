from person import Person


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