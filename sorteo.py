import random

def formato(cadena):
	if (len(i[0])<10):
		cadenaaux=i[0]
		for j in range(10-len(i[0])):
			cadenaaux=cadenaaux+' '
	else:
		cadenaaux=i[0]
	return cadenaaux
f = open('data.csv','w')
for i in range(500000):
	bombo1=[['Alemania',1], ['Brasil',5]  ,['Portugal',1] ,['Argentina',5] ,['Belgica',1]  ,['Polonia',1],['Francia',1]]
	bombo2=[['Espana',1]   ,['Peru',5]    ,['Suiza',1]    ,['Inglaterra',1],['Colombia',5] ,['Mexico',4] ,['Uruguay',5],['Croacia',1]]
	bombo3=[['Dinamarca',1],['Islandia',1],['CostaRica',4],['Suecia',1]    ,['Tunez',2]    ,['Egipto',2] ,['Senegal',2],['Iran',3]   ]
	bombo4=[['Serbia',1]   ,['Nigeria',2] ,['Australia',3],['Japon',3]     ,['Marruecos',2],['Panama',4] ,['Corea',3]  ,['Arabia',3] ]
	bombo2p=[]
	bombo3p=[]
	bombo4p=[]

	#Encabezados
	'''print ("|=======================================================================================|")
	print ("|Grupo 1   |Grupo 2   |Grupo 3   |Grupo 4   |Grupo 5   |Grupo 6   |Grupo 7   |Grupo 8   |")
	print ("|__________|__________|__________|__________|__________|__________|__________|__________|")'''


	#Elegir cabezas de serie
	cadena='|'
	random.shuffle(bombo1)
	bombo1.insert(0,['Rusia',1])
	'''for i in bombo1:
		cadena=cadena+formato(i[0])+"|"
	print (cadena)
	print ("|__________|__________|__________|__________|__________|__________|__________|__________|")'''



	#-----------------------------------
	#BOMBO2
	#-----------------------------------

	#elegir los grupos de sudamerica
	random.shuffle(bombo2)
	for i in range(8):
		bombo2p.append(['',0])

	listaaux=[]
	listaaux2=[]
	listagruposelegidos=[]
	for i in range(len(bombo1)):
		if (bombo1[i][1]!=5):
			listaaux.append(i)
		else:
			listaaux2.append(i)


	for i in bombo2:
		if (i[1]==5):
			elemento=random.choice(listaaux)
			listaaux.remove(elemento)
			bombo2p[elemento][0]=i[0]
			bombo2p[elemento][1]=i[1]
			listagruposelegidos.append([i[0],i[1]])
			#bombo2.remove([i[0],i[1]])


	for i in listagruposelegidos:
		bombo2.remove(i)

	for i in listaaux:
		listaaux2.append(i)

	#Determinar los grupos de los equipos restantes
	for i in range(len(bombo2)):
		elemento=random.choice(listaaux2)
		listaaux2.remove(elemento)
		bombo2p[elemento][0]=bombo2[0][0]
		bombo2p[elemento][1]=bombo2[0][1]
		bombo2.remove([bombo2[0][0],bombo2[0][1]])
		
	'''cadena='|'
	for i in bombo2p:
		cadena=cadena+formato(i[0])+'|'

	print (cadena)
	print ("|__________|__________|__________|__________|__________|__________|__________|__________|")'''

	#-----------------------------------
	#BOMBO3
	#-----------------------------------
	random.shuffle(bombo3)
	for i in range(8):
		bombo3p.append(['',0])

	#Determinar los grupos de los Europeos
	listaaux=[]
	listaaux2=[]
	listagruposelegidos=[]

	for i in range(8):
		noEuropeos=0
		if (bombo1[i][1]==1):
			noEuropeos=noEuropeos+1
		if (bombo2p[i][1]==1):
			noEuropeos=noEuropeos+1
		if (noEuropeos!=2):
			listaaux.append(i)
		else:
			listaaux2.append(i)

	for i in bombo3:
		if (i[1]==1):
			elemento=random.choice(listaaux)
			listaaux.remove(elemento)
			bombo3p[elemento][0]=i[0]
			bombo3p[elemento][1]=i[1]
			listagruposelegidos.append([i[0],i[1]])
			
	for i in listagruposelegidos:
		bombo3.remove(i)

	for i in listaaux2:
		listaaux.append(i)

	listaaux2=[]
	#Determinar el grupo de Costa Rica
	#Encontramos si esta disponible el grupo de mexico
	MEX=bombo2p.index(['Mexico',4])
	if(bombo3p[MEX][0]==''):
		#listaaux2.append(MEX)
		listaaux.remove(MEX)
		elemento=random.choice(listaaux)
		listaaux.remove(elemento)
		bombo3p[elemento][0]='CostaRica'
		bombo3p[elemento][1]=4
		bombo3.remove(['CostaRica',4])
		listaaux.append(MEX)
	#Determinamos los grupos de los demas eqipos en el bombo3
	for i in range(len(bombo3)):
		elemento=random.choice(listaaux)
		listaaux.remove(elemento)
		bombo3p[elemento][0]=bombo3[0][0]
		bombo3p[elemento][1]=bombo3[0][1]
		bombo3.remove([bombo3[0][0],bombo3[0][1]])



	'''cadena='|'
	for i in bombo3p:
		cadena=cadena+formato(i[0])+'|'

	print (cadena)
	print ("|__________|__________|__________|__________|__________|__________|__________|__________|")'''


	#-----------------------------------
	#BOMBO4
	#-----------------------------------

	for i in range(8):
		bombo4p.append(['',0])

	#Determinamos el Grupo de Serbia
	for i in range(8):
		aux=0
		if(bombo1[i][1]==1):
			aux=aux+1
		if(bombo2p[i][1]==1):
			aux=aux+1
		if(bombo3p[i][1]==1):
			aux=aux+1
		if(aux!=2):
			listaaux.append(i)
		else:
			listaaux2.append(i)

	elemento=random.choice(listaaux)
	listaaux.remove(elemento)
	bombo4p[elemento][0]='Serbia'
	bombo4p[elemento][1]=1
	bombo4.remove(['Serbia',1])
	#print ('Serbia, grupo: '+str(elemento))

	for i in listaaux2:
		listaaux.append(i)
	listaaux2=[]

	#Determinar el participante del grupo de Iran
	IRAN=bombo3p.index(["Iran",3])
	if bombo4p[IRAN][1]==0:
		
		tipos=[]
		tipos.append(bombo1[IRAN][1])
		tipos.append(bombo2p[IRAN][1])
		tipos.append(3)

		listaequiposaelegir=[]
		for i in bombo4:
			if (i[1] not in tipos):
				listaequiposaelegir.append(i)

		elemento=random.choice(listaequiposaelegir)
		bombo4p[IRAN][0]=elemento[0]
		bombo4p[IRAN][1]=elemento[1]
		bombo4.remove(elemento)

	#Determinar el Grupo de Panama

	listaaux=[]
	listaaux2=[]
	for i in range(len(bombo4p)):
		if bombo4p[i][1]==0:
			listaaux.append(i)

	if ['Panama',4] in bombo4:
		MEX=bombo2p.index(['Mexico',4])
		CTR=bombo3p.index(['CostaRica',4])
		if(MEX in listaaux):
			listaaux.remove(MEX)
			listaaux2.append(MEX)
		if(CTR in listaaux):
			listaaux.remove(CTR)
			listaaux2.append(CTR)
		elemento=random.choice(listaaux)
		listaaux.remove(elemento)
		bombo4p[elemento][0]="Panama"
		bombo4p[elemento][1]=4
		bombo4.remove(['Panama',4])

	for i in listaaux2:
		listaaux.append(i)

	#Elegir los eqipos africanos
	listaequiposaelegir=[]
	for i in bombo4:
		if i[1]==2:
			listaequiposaelegir.append(i)


	TUN=bombo3p.index(['Tunez',2])
	SEN=bombo3p.index(['Senegal',2])
	EGI=bombo3p.index(['Egipto',2])

	if TUN in listaaux:
		listaaux.remove(TUN)
	if SEN in listaaux:
		listaaux.remove(SEN)
	if EGI in listaaux:
		listaaux.remove(EGI)



	for i in listaequiposaelegir:
		elemento=random.choice(listaaux)
		listaaux.remove(elemento)
		bombo4p[elemento][0]=i[0]
		bombo4p[elemento][1]=i[1]
		bombo4.remove(i)

	listaaux=[]
	for i in range(len(bombo4p)):
		if bombo4p[i][1]==0:
			listaaux.append(i)

	#Elegir los grupos de los asiaticos aleatoriamente
	for i in range(len(bombo4)):
		elemento=random.choice(listaaux)
		listaaux.remove(elemento)
		#print (listaaux)
		bombo4p[elemento][0]=bombo4[0][0]
		bombo4p[elemento][1]=bombo4[0][1]
		bombo4.remove(bombo4[0])



	'''cadena='|'
	for i in bombo4p:
		cadena=cadena+formato(i[0])+'|'
	print (cadena)
	print ("|=======================================================================================|")
	'''
	#Creamos el archivo de datos
	 
	cadena=''
	for i in bombo1:
		cadena=cadena+i[0]+','

	for i in bombo2p:
		cadena=cadena+i[0]+','

	for i in bombo3p:
		cadena=cadena+i[0]+','

	for i in bombo4p:
		cadena=cadena+i[0]+','

	f.write (cadena[0:-1]+'\n')