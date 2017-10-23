class Cat():
	def __init__(self, jump, tail_length, mind):
		self.jump = jump
		self.tail_length = tail_length
		self.mind = mind

	def Meow(self):
		print('Мяу')

tom = Cat(100, 1, 500)
print(tom.tail_length)

barseek = Cat(20, 50, 0)
print(barseek.tail_length)