import random

elementos=[5,8,9,6,4,1,10,56]
capacidadMochila=70

def poblacionInicial(noCromosomas, noElementos):
	poblacion=[]
	for i in range(noElementos):
		cadena=''
		for i in range(noCromosomas):
			cadena=cadena+str(random.randrange(2))
		if [cadena,evaluarConjunto(cadena)] not in poblacion:
			poblacion.append([cadena,evaluarConjunto(cadena)])
	return poblacion

def evaluarConjunto(cadena):
	peso=0
	#print (elementos)
	for i in range(len(elementos)):
		if (cadena[i]=='1'):
			peso=peso+elementos[i]
	return peso

def evaluarPoblacion(poblacion):
	poblacionNueva=[]
	for i in poblacion:
		if i[1]<=capacidadMochila:
			poblacionNueva.append(i)
			#print (i+" "+str(poblacionNueva[i]))
	return poblacionNueva

def sortedDictValues1(adict):
    items = adict.items()
    items.sort()
    return [value for key, value in items]

#defina numero de elementos

longcromosomas=8
poblacion=poblacionInicial(longcromosomas,50)
poblacion=evaluarPoblacion(poblacion)
poblacion.sort(key=lambda sujeto: sujeto[1])
poblacion.reverse()
for i in poblacion:
	print (i)
