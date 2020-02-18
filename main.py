import numpy as np 
from numpy import poly1d
import control as ct 
import matplotlib.pyplot as plt 

#optionA
Gden = poly1d([1,10,100])

#optionB
#Gden = poly1d([1,15,100])

#optionC
#Gden = poly1d([1,5,100])

#optionD
#Gden = poly1d([1,20,100])

Gden = Gden.c
G = ct.tf([100],Gden)


t_end = 2
t = np.linspace(0,t_end,500)

x,y = ct.step_response(G,t)

overshoot = max(y)

plt.hlines(overshoot, xmin = 0, xmax = t_end, color = 'red')
plt.text(0,overshoot+0.02, overshoot, ha='left', va='center')
plt.plot(x,y)
plt.title("Option A")
plt.show()
