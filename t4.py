import cv2
import glob
import xlsxwriter
import numpy as np

# Camara 1 es la camara web integrada en mi caso||-1 es para externa
camara = 1
#Numero de fotogramas, mientras la camara se ajusta a los niveles de luz
fotogramas = 10

#iniciar camara
camera = cv2.VideoCapture(camara)

# Captura imagen  camara
def get_image():
 # leer la captura
 retval, im = camera.read()
 return im
for i in xrange(fotogramas):
 temp = get_image()
print("Foto tomada")
# entregar imagen leida anteriormente
imagen = get_image()
gris=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

file = "1izq.png"
# Guardar la imagen con opencv que fue leida por PIL
cv2.imwrite(file, gris)
print("foto guardada")

#eliminar lineatransportadora de la imagen

cv2.imwrite("sinnegro.png", negro)
# finalizar camara
del(camera)






#crear excel
listaFotos =  (glob.glob("*.png")) #lista de fotos
listaFotos.sort()
workbook = xlsxwriter.Workbook('Analisis.xlsx') #escribimos excel 
worksheet = workbook.add_worksheet('Desviacion Estandar')
worksheet2 = workbook.add_worksheet('Cuantificacion')
for i in range (len(listaFotos)):
    worksheet.write(i,0, listaFotos[i])
    worksheet2.write(i,0, listaFotos[i])
for f in range (len(listaFotos)):
    imagen = cv2.imread(listaFotos[f])
    (cuantificacion, desviacionEstandar) = cv2.meanStdDev(imagen) 
    # retorna 2 tuplas  significados de BGR (invertido)+ la desviacion
    worksheet2.write(f,1, cuantificacion[0])
    worksheet.write(f,1, desviacionEstandar[0])
workbook.close()
#fin exel