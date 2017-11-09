
#Local binary pattern in an image
#simport matplotlib.pyplot as plt
import numpy as np
import cv2

#Set the values of an image in the center pixel
#receive as input an image
def LbpHistogram(img):
	#We will use a auxiliar matrix of zeros
	aux=[]
	for i in range(256):
		aux.append(0)
	u=1
	#Find the values of LBP in all the posibles pixels
	for i in range(u,img.shape[0]-u):
		for j in range(u,img.shape[1]-u):
			#find the neighbor pixels
			px=[img.item(i-u,j-u), img.item(i-u,j), img.item(i-u,j+u), img.item(i,j+u), img.item(i+u,j+u), img.item(i+u,j), img.item(i+u,j-u), img.item(i,j-u)]
			#find if the pixels are major or minor than the center pixels
			suma=0
			for k in range(len(px)):
				if px[k]>=img.item(i,j):
					px[k]=1
					suma=suma+2**(len(px)-k-1)
				else:
					px[k]=0
			#print(suma)
			aux[suma]=aux[suma]+1
	return aux

