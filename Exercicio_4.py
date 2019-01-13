# -*- coding: utf-8 -*-

import math

#CREAMOS UNHA FUNCIÃ“N PARA COMPRABAR SE UN NÃšMERO Ã‰ PRIMO

def primo(numero):
	for n in range(2,int(math.sqrt(numero))+1):
		
		#COMPROBAMOS SE O NÃšMERO Ã‰ DIVISIBLE POR ALGÃšN NÃšMERO QUE NON SEXA 1 
		#	NIN EL MESMO
		
		if numero % n == 0:
		
			#EN CASO DE QUE O SEXA O NÃšMERO NON Ã‰ PRIMO
			
			return False
	
	#NO CADO DE QUE ACABE O BUCLE O NÃšMERO TEN QUE SER PRIMO
	
	return True

def primo_palindromo_cercano(numero):
	numero_pp = numero+1
	
	#CREAMOS UN BUCLE WHILE QUE COMPROBE SE O NÃšMERO Ã‰ PALINDROMO E PRIMO
	
	while not (primo(numero_pp) and str(numero_pp) == str(numero_pp)[::-1]):
	
		#SE NON O Ã‰ SUMAMOS 1 AO NÃšMERO
		
		numero_pp += 1
		
	return numero_pp
	
#PROBAMOS A PASARLLE UNHA LISTA DE NÃšMEROS A FUNCIÃ“N
		
lista_numeros = [2,6,13,101,168,545,1003]

for n in lista_numeros:
	print(u"O primo palindromo máis cercano a "+str(n)+u" é "+ 
		str(primo_palindromo_cercano(n)))