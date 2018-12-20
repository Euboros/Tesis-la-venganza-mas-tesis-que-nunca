import cv2
import numpy as np
import operator
import PIL

file = "linea.jpg"
linea=cv2.imread(file)
pxlinea = cv2.resize(linea, (1,1)) 
cv2.imshow('filtro', pxlinea)
cv2.imwrite("pixel de linea.jpg", pxlinea)

negro = np.array([0,0,0], dtype=np.uint8)
blanco=np.array([255,255,255], dtype=np.uint8)

#color=(pxlinea[0][0])
#print("color absoluto linea produccion",color)
colorlinea=np.array((pxlinea[0][0]),dtype=np.uint8)
print("color absoluto linea produccion:",colorlinea)

imagentomada=cv2.imread("foto2.jpg")

mascara = cv2.inRange(imagentomada, colorlinea, blanco)
cv2.imshow('filtro', mascara)
"""mascara= str(mascara).replace('[[', '')
mascara= str(mascara).replace(']]', '')
mascara= str(mascara).replace(' ', '')"""
#mascara=np.array([mascara], dtype=np.uint8)

print(mascara)
print(cv2.countNonZero(mascara))
abc=cv2.countNonZero(mascara)
alto,ancho=mascara.shape
print(alto*ancho)

if abc==(alto*ancho) :
	print("sirve")
else:
	print("no sirve")
while(1):
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
 
cv2.destroyAllWindows()


##filtro, toma una fotografia fondo la cual es la linea de produccion sin ninguna tabla
##luego la reduce a un pixel de 1x1 para generar mascara para consultar si la imagen tomada a posterior 
##es linea de produccion