from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

steps = np.linspace(0, 100, 101)
x_ave = np.zeros(101)
x_y0 = np.zeros(101)
x_now = np.zeros(3000)

for i in range(100):
    for j in range(3000):
        ruler = np.random.rand()
        if ruler<=0.5:
            x_now[j] = x_now[j] + 1
        else:
            x_now[j] = x_now[j] - 1
    average = sum(x_now)/3000
    x_ave[i+1] = average
    
plt.scatter(steps, x_ave,c='r')
plt.plot(steps, x_y0)
plt.xlim(0,100)
plt.ylim(-1,1)

plt.xlabel('step number')
plt.ylabel('<x>')

plt.show()


        