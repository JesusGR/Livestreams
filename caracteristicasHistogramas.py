import os
import cv2

def getHistogramaRGB(imagen):
	img=cv2.imread(imagen)
	histogramaR=[]
	histogramaG=[]
	histogramaB=[]
	for i in range(256):
		histogramaR.append(0)
		histogramaG.append(0)
		histogramaB.append(0)
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			histogramaB[img.item(i,j,0)]+=1
			histogramaG[img.item(i,j,1)]+=1
			histogramaR[img.item(i,j,2)]+=1
	for i in range(256):
		histogramaB[i]=float(histogramaB[i])/(img.shape[0]*img.shape[1])
		histogramaG[i]=float(histogramaG[i])/(img.shape[0]*img.shape[1])
		histogramaR[i]=float(histogramaR[i])/(img.shape[0]*img.shape[1])
	return [histogramaR, histogramaG, histogramaB]



print '@RELATION	BIRDS'

#for de tres canales
for i in range(3):
	#for de 0-255
	for j in range(256):
		print '@ATTRIBUTE	C'+str(i+1)+'I'+str(j)+'	REAL'

clases=''
for carpeta in os.listdir('images'):
	clases=clases+carpeta.split('.')[1]+','

print '@ATTRIBUTE	class	{'+clases+'}'
print '@DATA'

imagenes=os.listdir('images')
for carpeta in imagenes:
	for imagen in os.listdir('images/'+carpeta+'/'):
		if imagen.split('.')[-1]=='jpg':
			caracteristicas=''
			histogramas=getHistogramaRGB('images/'+carpeta+'/'+imagen)
			for i in histogramas:
				for j in i:
					caracteristicas=caracteristicas+str(j)+','
			caracteristicas=caracteristicas+carpeta.split('.')[1]
			print caracteristicas

