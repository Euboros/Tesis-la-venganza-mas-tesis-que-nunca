import cv2
import numpy as np
import time

#izquierda 1138-1
file = "izq.tif"
izq=cv2.imread(file)
izq=cv2.cvtColor(izq,cv2.COLOR_BGR2GRAY)
#derecha
file = "der.tif"
der=cv2.imread(file)
der=cv2.cvtColor(der,cv2.COLOR_BGR2GRAY)

(promedio) = cv2.mean(izq)
print(promedio[0])
#print(destandar) 
(promedio) = cv2.mean(der)
print(promedio[0])
#print(destandar) 
