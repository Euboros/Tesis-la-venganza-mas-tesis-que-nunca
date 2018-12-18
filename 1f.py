import cv2
import numpy as np
import operator

file = "fondo.png"
imagen=cv2.imread(file)
small = cv2.resize(imagen, (1,1)) 
cv2.imshow('filtro', small)
cv2.imwrite("resultado1f.png", small)

negro = np.array([0,0,0], dtype=np.uint8)
blanco=np.array([255,255,255], dtype=np.uint8)

color=(small[0][0])
grislinea=np.array((color),dtype=np.uint8)

mascara = cv2.inRange(small, blanco, grislinea)
mascara= str(mascara).replace('[[', '')
mascara= str(mascara).replace(']]', '')
mascara= str(mascara).replace(' ', '')
print(mascara)
mascara=np.array([mascara,mascara,mascara], dtype=np.uint8)
print(mascara)
print(negro)


if np.array_equal(negro,mascara):
	print("hola")

while(1):
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
 
cv2.destroyAllWindows()


##filtro, toma una fotografia fondo la cual es la linea de produccion sin ninguna tabla
##luego la reduce a un pixel de 1x1 para generar mascara para consultar si la imagen tomada a posterior 
##es linea de produccion