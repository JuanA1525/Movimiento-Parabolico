
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


t = np.arange(0, tMax+tMax/50, tMax/50)


Vx = Vi*np.cos(alpha)
X = (Xi + (Vx*t))
Xmax = ((Vi**2) / g) * (2*np.sin(alpha)*np.cos(alpha))

Vy = ((Vi*np.sin(alpha)) - (g*t))
Y = (Hi + (Vi*np.sin(alpha)*t) - ((0.5*g*t**2)))
Ymax = ((Vi**2) / (2*g))*(np.sin(alpha)**2)

Yx = (np.tan(alpha)*x) - ((g / ((2*(Vi**2))*(np.cos(alpha)**2)))*(x**2))

Ax = 0
Ay = -g

print(Xmax)
print(Ymax)
print()
print(np.cos(alpha))

fig, ax = plt.subplots(1,1, figsize = (15,5))
ax.plot(X, Y, lw=3)
ax.set_title("Trayectoria (x,y)", fontsize=25)
ax.set_xlabel('x [m]', fontsize=16)
ax.set_ylabel('y [m]', fontsize=16)
ax.grid(True, which='both')
#ax[0].set_xlim((-2, 280))
#ax[0].set_ylim((-2, 120))

fig.show()

input("HOla")

