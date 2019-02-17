import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
import array

prom=0
for z in range(1,4):
	img1= cv2.imread('i'+str(z)+'.tif',0)
	img2= cv2.imread('d'+str(z)+'.tif',0)
	alto, largo=img1.shape
	c1=[]
	c2=[]
	p=[]
	for i in range(largo):
		g1=0
		g2=0
		for j in range(0,alto):
			g1=img1[j][i]+g1
			g2=img2[j][i]+g2
		c1.append(g1/(alto))
		c2.append(g2/(alto))
	x=30
	x=math.radians(x)
	x=float(math.tan(x))
	for i in range(largo):
		p.append(c1[i]-c2[i]/float(c1[i]+c2[i])/float(x))
	
	


	x=np.empty(shape=largo)
	x=np.arange(largo)
	y=p
	
	plt.scatter(x, y)
	plt.show()