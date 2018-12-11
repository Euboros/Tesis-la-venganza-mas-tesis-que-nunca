import cv2
camera = cv2.VideoCapture(1)
# Captura imagen  camara
def get_image():
 # leer la captura
 retval, im = camera.read()
 return im
for i in xrange(1):
 temp = get_image()
print("Foto tomada")
# entregar imagen leida anteriormente
camera_capture = get_image()
file = "wea.png"
cv2.imwrite(file, camera_capture)
del(camera)