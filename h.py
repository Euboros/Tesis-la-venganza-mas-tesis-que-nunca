#haralik
import cv2
import numpy as np
import math
from time import time
tiempo_inicial = time() 

'''
camara = 0
fotogramas = 10
camera = cv2.VideoCapture(camara)
def get_image():
	retval, im = camera.read()
	return im
for i in xrange(fotogramas):
 temp = get_image()
img = get_image()

raw_input("press")

for i in xrange(fotogramas):
 temp = get_image()
img2 = get_image()

'''
print("40")
img = cv2.imread('40a.jpg')
img2 = cv2.imread('40b.jpg')
tiempo_fotos=time()
alto, largo,chanels = img.shape

#cv2.imwrite('img.jpg', img)
#cv2.imwrite('img2.jpg', img2)
img[:, :, 0] = 0
img2[:, :, 0] = 0
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2=cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


#Hacer roi
c=400
ejey=alto/2-c/2
ejeyy=alto/2+c/2
ejex=largo/2-c/2
ejexx=largo/2+c/2
img = img[ejey:ejeyy,ejex:ejexx]
img2=img2[ejey:ejeyy,ejex:ejexx]

cv2.imwrite('img cortada.jpg', img)
cv2.imwrite('img2 cortada.jpg', img2)

alto, largo = img.shape

#print("x:"+str(ejex)+" y:"+str(ejey))
#print("x:"+str(ejexx)+" y:"+str(ejeyy))


mo=np.zeros(shape=(256, 256), dtype=int) ##matriz glcm
mcombi=np.zeros(shape=(alto, largo), dtype='int64') ##matriz con la diferencia entre tonos de grises para 2 fotos

for i in range(alto):#se llena la matriz mcombi con la diferencia entre grises para 2 imagenes
	for j in range (largo):
		#raw_input("Press Enter to continue...")
		aux=int(img[i][j])#hacer casteo pues el valor entero sale en 8bits
		aux2=int(img2[i][j])
		mcombi[i][j]=abs((aux+aux2)/2)
		#print("i:"+str(i)+" j:"+str(j))
		#print("aux="+str(aux)+" aux2="+str(aux2))		
		#print("num:"+str(mcombi[i][j]))
	

#mcombi.sort(axis=0) ordena matriz

cv2.imwrite('enfrentada.jpg', mcombi)

for i in range(alto):#se llena la matriz mo con la acumulacion de intencidad de grises a partir de la matriz mcombi
	for j in range (largo-1):
		#raw_input("Press Enter to continue...")
		aux=mcombi[i][j]
		aux2=mcombi[i][j+1]			
		aux3=mo[aux][aux2]
		aux3=aux3+1
		mo[aux][aux2]=aux3



ms=np.zeros(shape=(256, 256), dtype=int) #matriz simetrica

sum=0

for i in range(256):#se simetriza la matriz mo en la matriz ms
	for j in range(256):
		ms[i][j]=mo[i][j]+mo[j][i]
		
		sum=sum+ms[i][j]

mp=np.zeros(shape=(256, 256), dtype=float) #matriz de probabilidad


for i in range(256):#llenamos la matriz mp con probabilidades
	for j in range(256):
		mp[i][j]=ms[i][j]/float(sum)
		

o = 0.0 # tetha
u = 0  #valor mu antes de promediar
for i in range (256):
    for j in range (256):
        u = u + i
        den = 0.0
        den = u/float((i)+1)
        den = (i) - den
        den = den*den  
        wea=(mp[i][j])
        o = o + (wea)*(den)
        
raiz=math.sqrt(o)
print("desviacion estandar:"+str(raiz))

tiempo_final = time() 
te = tiempo_final - tiempo_fotos
ti=tiempo_fotos-tiempo_inicial
#print(te)
print("tiempo ejecucion:"+str(ti))
##hacemos una matriz con la diferencia de los coeficientes de grises, dps hacemos el resto de mierda##