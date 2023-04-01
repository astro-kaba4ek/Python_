# coding: utf-8

class Angle(object):
	"""Simple operations with angles."""
	
	def __init__(self, d, m, s):
		self.d = d 
		self.m = m 
		self.s = s
	

	@classmethod 
	def from_decimal(cls, x):
		d = int(abs(x))
		m = int((abs(x)-d) * 60)
		s = (((abs(x)-d) * 60) % 1) * 60

		if x < 0: d = -d

		return cls(d, m, s)


	def decimal(self):
		x = abs(self.d) + self.m/60 + self.s/3600

		if self.d < 0: x = -x

		return x
	

	def __neg__(self):
		return Angle(-self.d, self.m, self.s)


	def __add__(self, other):
		x_new = self.decimal() + other.decimal()

		return Angle.from_decimal(x_new)
	

	def __sub__(self, other):
		x_new = self.decimal() - other.decimal()

		return Angle.from_decimal(x_new)


	def show(self):
		print(self.d, self.m, round(self.s, 3))
	



# phi = Angle.from_decimal(float(input("Введите широту наблюдения в градусах: ")))
# delta = Angle.from_decimal(float(input("Введите сколнение завезды в градусах: ")))


phi = list(map(float, input("Введите широту наблюдения в градусах, минутах и секундах: ").split()))
phi = Angle(phi[0], phi[1], phi[2])

delta = list(map(float, input("Введите сколнение завезды в градусах, минутах и секундах: ").split()))
delta = Angle(delta[0], delta[1], delta[2])


phi.show()
delta.show()

if phi.decimal() >= delta.decimal():
	h_u = Angle.from_decimal(90) - phi + delta
else:
	h_u = Angle.from_decimal(90) + phi - delta

h_u.show()