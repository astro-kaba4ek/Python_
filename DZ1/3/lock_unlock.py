# coding: utf-8
from random import randint

class Lock(object):
	def __init__ (self, p):
		self.password = str(p)
	
	def unlock(self, x):
		x = str(x)
		n = len(x)

		if x == self.password:
			return "success"

		elif n != len(self.password):
			return "wrong length"

		else:
			true_index = []
			for i in range(0, n):
				if self.password[i] == x[i]: true_index.append(i)
			return true_index


def lock_unlock(x):
	attempt = list("0")
	answer = x.unlock("".join(attempt))

	while answer != "success":
		print("attempt:", "".join(attempt))
		print("answer:", answer, "\n")

		if answer == "wrong length":
			attempt.append("0")
		else:
			for i in range(0, len(attempt)):
				if i not in answer:
					attempt[i] = str(int(attempt[i]) + 1)
					
		answer = x.unlock("".join(attempt))

	print("attempt:", "".join(attempt))
	print("answer:", answer, "\n")

	return x.password






parol = randint(0, 1000000)
print("parol =", parol, "\n")
slozhnyi_parol = Lock(parol)

true_password = lock_unlock(slozhnyi_parol)
print("Поздравляю! \npassword =", true_password)



