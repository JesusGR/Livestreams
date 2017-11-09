import os
import cv2
import numpy as np

def ViolaJonesBoca(nombreImagen,aimg):
	img=cv2.imread(nombreImagen,0)
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	faces=face_cascade.detectMultiScale(img, 1.4, 6)
	if len(faces)>0:
		x=faces[0][0]
		y=faces[0][1]
		w=faces[0][2]
		h=faces[0][3]
	
		'''mouth=[]
		for i in range(y,y+w):
			mouth.append([])
			for j in range(x,x+h):
				#print "i:",i,"j",j
				mouth[-1].append(img.item(i,j))'''
		mouth=[]
		for i in range(y+int(w*.6),y+w):
			mouth.append([])
			for j in range(x+int(h*.2),x+int(h*.8)):
				#print "i:",i,"j",j
				mouth[-1].append(aimg.item(i,j))
		mouth=np.asarray(mouth)
		return mouth

def ViolaJones(nombreImagen,aimg):
	img=cv2.imread(nombreImagen,0)
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	faces=face_cascade.detectMultiScale(img, 1.4, 6)
	if len(faces)>0:
		x=faces[0][0]
		y=faces[0][1]
		w=faces[0][2]
		h=faces[0][3]
		ojo_izquierdo=[]
		for i in range(y+int(w*.28),y+int(w*.5)):
			ojo_izquierdo.append([])
			for j in range(x+int(h*.1),x+int(h*.5)):
				#print "i:",i,"j",j
				ojo_izquierdo[-1].append(aimg.item(i,j))
		ojo_izquierdo=np.asarray(ojo_izquierdo)

		ojo_derecho=[]
		for i in range(y+int(w*.28),y+int(w*.5)):
			ojo_derecho.append([])
			for j in range(x+int(h*.5),x+int(h*.9)):
				#print "i:",i,"j",j
				ojo_derecho[-1].append(aimg.item(i,j))
		ojo_derecho=np.asarray(ojo_derecho)

		mouth=[]
		for i in range(y+int(w*.6),y+w):
			mouth.append([])
			for j in range(x+int(h*.2),x+int(h*.8)):
				#print "i:",i,"j",j
				mouth[-1].append(aimg.item(i,j))
		mouth=np.asarray(mouth)

		ceja_izquierda=[]
		for i in range(y+int(w*.2),y+int(w*.4)):
			ceja_izquierda.append([])
			for j in range(x+int(h*.1),x+int(h*.5)):
				#print "i:",i,"j",j
				ceja_izquierda[-1].append(aimg.item(i,j))
		ceja_izquierda=np.asarray(ceja_izquierda)

		ceja_derecha=[]
		for i in range(y+int(w*.2),y+int(w*.4)):
			ceja_derecha.append([])
			for j in range(x+int(h*.5),x+int(h*.9)):
				#print "i:",i,"j",j
				ceja_derecha[-1].append(aimg.item(i,j))
		ceja_derecha=np.asarray(ceja_derecha)

		rostro=[]
		for i in range(y,y+w):
			rostro.append([])
			for j in range(x,x+h):
				#print "i:",i,"j",j
				rostro[-1].append(aimg.item(i,j))
		rostro=np.asarray(rostro)

		return [ojo_izquierdo,ojo_derecho,mouth,ceja_izquierda,ceja_derecha,rostro]
