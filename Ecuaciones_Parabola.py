from cProfile import label
import tkinter
from tkinter.ttk import LabeledScale
from turtle import color
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt

import json



#@title DATOS NECESARIOS (Ojo, el angulo es necesario):

try:
  
  angulo = 12 #@param {type:"number"}
  #@markdown Ingrese la velocidad inicial:
  Vi = 0 #@param {type:"number"}
  #@markdown Ingrese la altura inicial:
  Hi = 2 #@param {type:"number"}
  #@markdown Ingrese la altura final:
  Hf = -6 #@param {type:"number"}
  #@markdown Ingrese la posicion inicial:
  Xi = 0 #@param {type:"number"}
  #@markdown Ingrese la posicion final:
  Xf = 0 #@param {type:"number"}
  #@markdown Ingrese el tiempo maximo:
  tMax = 6 #@param {type:"number"}

  g = 9.776

  if Hi == None:
    Hi = 0

  if Xi == None:
    Xi = 0

  if Xf == None:
    Xf = 0

  if Hf == None:
    Hf == 0

  if tMax == None:
    tMax = 0

  alpha = ((angulo * np.pi) / 180)
  #tMax = 2*Vi*np.sin(alpha)/g 

  if Vi == 0 or Vi == None:
    Vi = (g*tMax)/2*np.sin(alpha)

  raiz = (((Vi**2)*(np.sin(alpha)**2)) + 2*g*Hi)

  if raiz < 0:
      print(raiz)
      print("\nTu Parabola NO sale de la tierra. Intenta con otros valores\n")

  else:

    tMax2 = (((Vi*np.sin(alpha)) + (np.sqrt(((Vi**2)*(np.sin(alpha)**2)) -2*g*Hf + 2*g*Hi))) / g)
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
    xXmax = Xi + (Vx*tMax2)

    fig, ax = plt.subplots(1,2, figsize = (15,5))
    ax[0].plot(X, Y,'k--',lw=3)
    ax[0].set_title("Trayectoria (x,y)", fontsize=25)
    ax[0].set_xlabel('x [m]', fontsize=16)
    ax[0].set_ylabel('y [m]', fontsize=16)
    ax[0].grid(True, which='both')
    ax[0].plot(xHmax,Ymax,'s',lw=4, label = (f'Altura Max: ({np.round(xHmax,2)}, {np.round(Ymax,2)})'))
    ax[0].plot(xXmax,Hf,'o',lw=4, label=f'Distancia Max: ({np.round(xXmax,2)}, {Hf})')
    ax[0].plot(Xi,Hi,'v',lw=4,label=f'Posicion Inicial: ({Xi}, {Hi})')
    ax[0].plot(lw=4,label=f'Velocidad Generada: ({np.round(Vi, 2)})')
    ax[0].legend()

    ax[1].plot(X, Y,'k--',lw=3)
    ax[1].set_title("Trayectoria (x,y)", fontsize=25)
    ax[1].set_xlabel('x [m]', fontsize=16)
    ax[1].set_ylabel('y [m]', fontsize=16)
    ax[1].grid(True, which='both')
    ax[1].plot(xHmax,Ymax,'s',lw=4, label = (f'Altura Max: ({np.round(xHmax,2)}, {np.round(Ymax,2)})'))
    ax[1].plot(xXmax,Hf,'o',lw=4, label=f'Distancia Max: ({np.round(xXmax,2)}, {Hf})')
    ax[1].plot(Xi,Hi,'v',lw=4,label=f'Posicion Inicial: ({Xi}, {Hi})')
    ax[1].plot('o', lw=4,label=f'Velocidad Generada: ({np.round(Vi, 2)})')
    ax[1].legend()

    fig.show()
    input("")
except:
  print("No se puede calcular debido a la falta de datos necesarios.")