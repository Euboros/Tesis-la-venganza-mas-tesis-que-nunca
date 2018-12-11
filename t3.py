import cv2
import glob
import xlsxwriter

# Camara 1 es la camara web integrada en mi caso||-1 es para externa
camara = 1
#Numero de fotogramas, mientras la camara se ajusta a los niveles de luz
fotogramas = 1

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
camera_capture = get_image()
camera_capture=cv2.cvtColor(camera_capture,cv2.COLOR_BGR2GRAY)
ddepth = cv2.CV_16S
kernel_size = 1000000
camera_capture=cv2.Laplacian(camera_capture, ddepth, kernel_size)
file = "captura2.png"
# Guardar la imagen con opencv que fue leida por PIL
cv2.imwrite(file, camera_capture)
print("foto guardada")


# finalizar camara
del(camera)


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
