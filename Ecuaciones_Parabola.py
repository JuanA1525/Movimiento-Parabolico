
from cProfile import label
from tkinter.ttk import LabeledScale
from turtle import color
import numpy as np
import matplotlib.pyplot as plt


grad = 45
g = 9.8
Hi = 0.264
Vi = 3
Xi = 0
x = np.arange(0, 10, 1)

alpha = ((grad * np.pi) / 180)
tMax = 2*Vi*np.sin(alpha)/g 

tMax2 = (((Vi*np.sin(alpha)) + (np.sqrt(((Vi**2)*(np.sin(alpha)**2)) + 2*g*Hi))) / g)


#t = np.arange(0, tMax+tMax/50, tMax/50)
t = np.arange(0, tMax2+tMax2/50, tMax2/50)


Vx = Vi*np.cos(alpha)
X = (Xi + (Vx*t))
Xmax = (((Vi**2)*(2*np.cos(alpha)*np.sin(alpha))) / g)

Vy = ((Vi*np.sin(alpha)) - (g*t))
Y = (((Vi*np.sin(alpha)*t) - (0.5*g*t**2)) + Hi)
Ymax = ((((Vi**2)*(np.sin(alpha)**2)) / (2*g)) + Hi)

tHmax = ((Vi*np.sin(alpha))/g)
xHmax = Xi + (Vx*tHmax)

tXmax = tMax2
xXmax = Xi + (Vx*tXmax)
#x = v0*np.cos(theta0)*t
#y = v0*np.sin(theta0)*t - 0.5*g*t**2

#Yx = (np.tan(alpha)*x) - ((g / ((2*(Vi**2))*(np.cos(alpha)**2)))*(x**2))

fig, ax = plt.subplots(1,1, figsize = (15,5))
ax.plot(X, Y,'k--',lw=3)
ax.set_title("Trayectoria (x,y)", fontsize=25)
ax.set_xlabel('x [m]', fontsize=16)
ax.set_ylabel('y [m]', fontsize=16)
ax.grid(True, which='both')
ax.plot(xHmax,Ymax,'s',lw=4, label = ('Altura Max'))
#ax.scatter(xHmax,Ymax)
ax.plot(xXmax,0,'o',lw=4, label='Distancia Max')
ax.plot(Xi,Hi,'v',lw=4,label='Posicion Inicial')
ax.legend()
#ax.scatter(1.29,0)
#ax[0].set_xlim((-2, 280))
#ax[0].set_ylim((-2, 120))

fig.show()

input("HOla")

