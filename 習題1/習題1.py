import matplotlib.pyplot as plt
import numpy as np
import random as rd

# x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
# y = np.array([2, 3, 4, 5, 6], dtype=np.float32)
x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
y = np.array([1.9, 3.1, 3.9, 5.0, 6.2], dtype=np.float32)

def predict(a, xt):
	return a[0]+a[1]*xt

def MSE(a, x, y):
	total = 0
	for i in range(len(x)):
		total += (y[i]-predict(a,x[i]))**2
	return total

def loss(p):
	return MSE(p, x, y)

# p = [0.0, 0.0]
# plearn = optimize(loss, p, max_loops=3000, dump_period=1)
def optimize(P):
	
	failCount = 0
	MaxEpisodes = 10000
	i=0
	while True:
		i+=1
		s1 = rd.randint(-1,1)*rd.random()*0.001
		s2 = rd.randint(-1,1)*rd.random()*0.001
		nextP = [P[0]+s1 , P[1]+s2]
		print('i=', i, 'P=', P, 'fail=', failCount, 'loss=', loss(P), 'loss(nextP)=', loss(nextP))
		if (s1==0 and s2==0) or loss(P) < loss(nextP): 
			failCount += 1
		else:
			P = nextP
			failCount = 0

		if failCount >= MaxEpisodes: 
			return P
		

P = [0,0]
p = optimize(P)

# Plot the graph
y_predicted = list(map(lambda t: p[0]+p[1]*t, x))
print('y_predicted=', y_predicted)
plt.plot(x, y, 'ro', label='Original data')
plt.plot(x, y_predicted, label='Fitted line')
plt.legend()
plt.show()