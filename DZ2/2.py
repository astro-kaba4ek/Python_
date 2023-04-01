#coding: utf-8

import numpy as np
import time 
from matplotlib import pyplot as plt
from scipy import odr

def f1(B, x):
	return B[0]*x + B[1]

def f2(B, x):
	return B[0]*x**2 + B[1]*x + B[2]

def f3(B, x):
	return B[0]*x**3 + B[1]*x**2 + B[2]*x + B[3]


NN = 100

list_N = [N for N in range(1, NN+1, 10)]

t = []
t_np = []

AA = np.random.random(NN)
BB = np.random.random(NN)

for N in list_N:

	A = AA[:N]
	B = BB[:N]

	tt = 0
	tt_np = 0
	for n in range(100):

		t0 = time.time()
		for i in range(N):
			c = A[i] * B[i]
		t1 = time.time()

		tt += (t1-t0)

		t0 = time.time()
		c = A * B
		t1 = time.time()

		tt_np += (t1-t0)

	t.append(tt/100)
	t_np.append(tt_np/100)

linear_model = odr.Model(f1)
data = odr.Data(list_N, t)
job = odr.ODR(data, linear_model, beta0=[0., 0.])
results = job.run()
y = results.beta[0] * np.array(list_N) + results.beta[1]

plt.subplot(131)
plt.ylabel("t")
plt.title("Dimension = 1")
plt.plot(list_N, t, 'b.', list_N, t_np, 'r.')
plt.plot(list_N, y, "g-")



t = []
t_np = []

AA = np.random.random((NN, NN))
BB = np.random.random((NN, NN))

for N in list_N:

	A = AA[:N, :N]
	B = BB[:N, :N]

	tt = 0
	tt_np = 0
	for n in range(10):

		t0 = time.time()
		for i in range(N):
			for j in range(N):
	 			c = A[i][j] * B[i][j]
		t1 = time.time()

		tt += (t1-t0)

		t0 = time.time()
		c = A * B
		t1 = time.time()

		tt_np += (t1-t0)

	t.append(tt/10)
	t_np.append(tt_np/10)

quadratic_model = odr.Model(f2)
data = odr.Data(list_N, t)
job = odr.ODR(data, quadratic_model, beta0=[0., 0., 0.])
results = job.run()
y = results.beta[0] * np.array(list_N)**2 + results.beta[1] * np.array(list_N) + results.beta[2]

plt.subplot(132)
plt.title("Dimension = 2")
plt.xlabel("N")
plt.plot(list_N, t, 'b.', list_N, t_np, 'r.')
plt.plot(list_N, y, "g-")



t = []
t_np = []

AA = np.random.random((NN, NN, NN))
BB = np.random.random((NN, NN, NN))

for N in list_N:

	A = AA[:N, :N, :N]
	B = BB[:N, :N, :N]

	tt = 0
	tt_np = 0
	for n in range(5):

		t0 = time.time()
		for i in range(N):
			for j in range(N):
				for k in range(N):
					c = A[i][j][k] * B[i][j][k]
		t1 = time.time()

		tt += (t1-t0)

		t0 = time.time()
		c = A * B
		t1 = time.time()

		tt_np += (t1-t0)

	t.append(tt/5)
	t_np.append(tt_np/5)

cubic_model = odr.Model(f3)
data = odr.Data(list_N, t)
job = odr.ODR(data, cubic_model, beta0=[0., 0., 0., 0.])
results = job.run()
y = results.beta[0] * np.array(list_N)**3 + results.beta[1] * np.array(list_N)**2 + results.beta[2] * np.array(list_N) + results.beta[3]

plt.subplot(133)
plt.title("Dimension = 3")
plt.plot(list_N, t, 'b.', list_N, t_np, 'r.')
plt.plot(list_N, y, "g-")


plt.show()