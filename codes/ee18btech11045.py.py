import numpy as np 
from numpy import poly1d
import control as ct 
import matplotlib.pyplot as plt 

Gden = poly1d([1,10,100])

Gden = Gden.c
G = ct.tf([100],Gden)

t_end = 2
t = np.linspace(0,t_end,500)

x,y = ct.step_response(G,t)

overshoot = max(y)
final_value = y[len(t)-1]

plt.hlines(overshoot, xmin = 0, xmax = t_end, color = 'red')
plt.text(0,overshoot+0.02, overshoot, ha='left', va='center')

plt.hlines(final_value, xmin = 0, xmax = t_end, color = 'red')
plt.text(0,final_value+0.02, final_value, ha='left', va='center')

plt.plot(x,y)
plt.xlabel("time")
plt.ylabel("c(t)")
plt.show()