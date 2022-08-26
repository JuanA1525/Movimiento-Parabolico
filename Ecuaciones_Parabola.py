from logging import exception
from cProfile import label
import tkinter
from tkinter.ttk import LabeledScale
from turtle import color
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt

import json



#@title DIngreso de Datos: Angulo necesario, Tmax o Vi Necesarios.

try:
  
  angulo = 70 #@param {type:"number"}
  #@markdown Ingrese la velocidad inicial:
  Vi = 3 #@param {type:"number"}
  #@markdown Ingrese la altura inicial:
  Hi = 0.263 #@param {type:"number"}
  #@markdown Ingrese la altura final:
  Hf = None #@param {type:"number"}
  #@markdown Ingrese la posicion inicial:
  Xi = None #@param {type:"number"}
  #@markdown Ingrese el tiempo maximo:
  tMax = None #@param {type:"number"}

  g = 9.776

  if Hi == None:
    Hi = 0

  if Xi == None:
    Xi = 0

  if Hf == None:
    Hf = 0

  if tMax == None:
    tMax = 0

  alpha = ((angulo * np.pi) / 180)
  #tMax = 2*Vi*np.sin(alpha)/g 

  if Vi == 0 or Vi == None:
    Vi = (g*tMax)/2*np.sin(alpha)

  raiz = (((Vi**2)*(np.sin(alpha)**2)) - (2*g*Hf) + (2*g*Hi))

  if raiz < 0:
      print("\nNO ES POSIBLE CALCULAR UNA PARABOLA CON LOS DATOS INGRESADOS.\nINTENTA CON OTROS VALORES")

  else:

    tMax2 = (((Vi*np.sin(alpha)) + (np.sqrt(((Vi**2)*(np.sin(alpha)**2)) - (2*g*Hf) + (2*g*Hi)))) / g)
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
    xYmax = (((Vi*np.sin(alpha)*tMax2) - (0.5*g*tMax2**2)) + Hi)

    Vxf = Vx
    Vyf = ((Vi*np.sin(alpha)) - (g*tMax2))
    Vf = np.sqrt((Vxf**2) + (Vxf**2))

    angFinal = (((np.arctan((Vyf)/(Vxf))) * 180) / np.pi)

    fig, ax = plt.subplots(1,1, figsize = (15,5))
    ax.plot(X, Y,'k--',lw=3)
    ax.set_title("Trayectoria (x,y)", fontsize=25)
    ax.set_xlabel('x [m]', fontsize=16)
    ax.set_ylabel('y [m]', fontsize=16)
    ax.grid(True, which='both')
    ax.plot(xHmax,Ymax,'s',lw=4, label = (f'Altura Max: ({np.round(xHmax,2)}, {np.round(Ymax,2)})'))
    ax.plot(xXmax,Hf,'o',lw=4, label=f'Distancia Max: ({np.round(xXmax,2)}, {Hf})')
    ax.plot(Xi,Hi,'v',lw=4,label=f'Posicion Inicial: ({Xi}, {Hi})')
    ax.plot(lw=4,label=f'Velocidad Generada: ({np.round(Vi, 2)})')
    ax.legend()

    fig.show()

    print(f"""  
  De acuerdo a los datos ingresados, los datos Finales son:

    TIEMPOS:
      - Tiempo de Vuelo: ({np.round(tMax2,2)} s)
      - Tiempo para Altura Maxima: ({np.round(tHmax,2)} s)

    VELOCIDADES:
      - Velocidad Inicial: ({Vi} m/s)
      - Velocidad Final: ({np.round(Vf,2)} m/s)

    POSICIONES:
      - Posicion Inicial: ({np.round(Xi,2)}, {np.round(Hi,2)})
      - Posicion Final: ({np.round(xXmax,2)}, {np.round(xYmax,2)})

    DISTANCIAS:
      - Distancia Maxima Recorrida: ({np.round(xXmax,2)} m)
      - Altura Maxima Alcanzada: ({np.round(Ymax,2)} m)

    ANGULOS:
      - Ángulo Inicial: ({angulo})
      - Ángulo Final: ({np.round(angFinal,2)})
    
  Gracias Por Utilizar Nuestro Sistema. 
    """)
except(exception):
  print(exception)
  print("No se puede calcular debido a la falta de datos necesarios.")

input("")