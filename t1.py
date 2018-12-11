import cv2
from math import sin #para usar la funcion seno
from time import time #importamos la funcion time para capturar tiempos

# Camara 1 es la camara web integrada en mi caso
camara = 1
#Numero de fotogramas, mientras la camara se ajusta a los niveles de luz
fotogramas = 1
tiempo_inicial = time() 
#iniciar camara
camera = cv2.VideoCapture(camara)
tiempo_final = time() 
tiempo_ejecucion = tiempo_final - tiempo_inicial
print("El tiempo de ejecucion fue:",tiempo_ejecucion)
# Captura imagen  camara
def get_image():
 # leer la captura
 retval, im = camera.read()
 return im
for i in xrange(fotogramas):
 temp = get_image()
print("Foto tomada")
# entregar imagen leida anteriormente
camera_capture = get_image()

file = "captura.png"
# Guardar la imagen con opencv que fue leida por PIL
cv2.imwrite(file, camera_capture)
print("foto guardada")

# finalizar camara
del(camera)