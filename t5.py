import cv2
import numpy as np
import time
 
#foto de muestra de la linea
camara = 1
fotogramas = 10
camera = cv2.VideoCapture(camara)
def get_image():
	retval, im = camera.read()
	return im
for i in xrange(fotogramas):
 temp = get_image()
print("Foto muestra tomada")
imagen = get_image()
file = "muestrap5.png"
cv2.imwrite(file, imagen)
del(camera)
raw_input("continuar")



hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
 
#Rango de colores detectados:
#Verdes:
negro = np.array([0,0,0], dtype=np.uint8)
gris = np.array([160,160, 160], dtype=np.uint8)

#Crear las mascaras
mascara = cv2.inRange(hsv, negro, gris)



#Mostrar la mascara final y la imagen
cv2.imshow('mascara', mascara)
cv2.imshow('Imagen', imagen)
#Salir con ESC
while(1):
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
 
cv2.destroyAllWindows()


#sacra foto al inicio y dejar el pixel mas claro como cota superior para la mascara