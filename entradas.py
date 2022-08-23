
import numpy as np

grad = 0
t = 0
g = 9.8
Hi = 0
Vi = 0
Xi = 0
x = 0

alpha = (grad * np.pi) / 180

Vx = Vi*np.cos(alpha)
X = Xi + (Vx*t)
Xmax = (((Vi**2) / g) * np.sin(2*alpha))

Vy = ((Vi*np.sin(alpha)) - (g*t))
Y = (Hi + (Vi*np.sin(alpha)*t) - ((g*t**2) / 2))
Ymax = ((Vi**2) / (2*g))*(np.sin(alpha)**2)

Yx = (np.tan(alpha)*x) - ((g / ((2*(Vi**2))*(np.cos(alpha)**2)))*(x**2))

Ax = 0
Ay = -g

