# plot ln(n) against n

import matplotlib.pyplot as plt
import math

N = range (1, 1000)
lnN = []

for n in N:
	lnN.append(math.log(n))


plt.plot(N, lnN)
plt.xlabel('Number of Nodes')
plt.ylabel('ln(Number of Nodes)')
plt.title('Simple Plot: How ln(n) varies with n, as n increases (n=nodes)')
plt.show()

