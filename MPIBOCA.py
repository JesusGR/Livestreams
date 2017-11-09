import os
import cv2
import ViolaJonesImagen as VJ
import LBP

directorio='../Tesis_Maestria/Bases_Datos/JaffeDataset/'
f = open('data.txt','w') 
#print ("Comenzando Proceso...")
encabezados=""
for i in range(256):
	encabezados=encabezados+"H"+str(i)+","
encabezados=encabezados+"class"
f.write(encabezados+'\n')
for dirName, subdirList, fileList in os.walk(directorio):
	for fname in fileList:
		#print (fname)
		if fname.split('.')[-1]=='tiff':
			#Find the Regions of intetrest of the subjects
			ROIs=cv2.split(cv2.imread(directorio+fname))[1]
			ROIs=VJ.ViolaJones(directorio+fname,ROIs)
			#cv2.imwrite("Rostros/"+fname.split('.')[0]+fname.split('.')[1]+".bmp",ROIs[5])
			#Get LBP histogram
			#print(fname)
			LBPHistogram=LBP.LbpHistogram(ROIs[5])
			features=""
			for i in LBPHistogram:
				features=features+str(float(i))+", "
			features=features+fname.split(".")[1][0:2]
			f.write (features+'\n')
			#print(LBP.LbpHistogram(ROIs[0]))
