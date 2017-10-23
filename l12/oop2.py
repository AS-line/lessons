class Animal:
	def __init__(self, hands, areal, feed):
		self.hands = hands
		self.areal = areal
		self.feed = feed

	def scream(self, name):
		print('AAAAAAA! Where is my ' + name + '???')
		print('Я хочу есть '+ self.feed)
	def attack(self, victim):
		print('Набросился на ')
# howler = Animal(4, 'Россия', 'нытьё')
# print('Ревун обитает в '+ howler.areal)

# howler.scream('Комп')

class Fish(Animal):
	def swim(self, speed):
		print('вжух-вжух-вжух-' * speed)

# arkadi = Fish(0, 'Ак-гёль', 'мусор')
# arkadi.scream('ДИИИММОООННН!!')
# arkadi.swim(5)

class Birds(Animal):
	def __init__(self, wings, areal, feed, highs):
		self.wings = wings
		self.areal = areal
		self.feed = feed
		self.highs = highs


	def scream(self):
		print("Супер КАААР!")
	def attak(self):
		print('sdvxc '+ self.wings)

# kar_karich = Birds(3, 'Чернобыль', 'Бандиты', -10)
# kar_karich.scream()

class ElvilBirds(Birds):
	def __init__(self, wings, areal, feed, highs, fangs):
		super().__init__(wings, areal, feed, highs)
		self.fangs = fangs
	def scream(self):
		super().scream()
		print("UUU")

red = ElvilBirds(2, 'Везде', 'Мясо!', 1000000, 1)
print(red.fangs)
red.scream()
