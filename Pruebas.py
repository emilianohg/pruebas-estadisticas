import math
import matplotlib.pyplot as plt
import scipy.stats as sct
from random import random
from tabulate import tabulate

#AQUI COMIENZA LO IMPORTANTE
#ESTA PRIMERA FUNCIÓN LO UNICO QUE HACE ES ASIGNAR EL ESPACIO DONDE SE GENERAN LAS DUPLAS
#ESTO LO HICE PORQUE SINO REPETIA MUCHO CODIGO
#EJEMPLO SI x,y es igual a 1,1 SIGNIFICA QUE PERTENECE AL RANGO DE >0.2,>0.2
def getCoord(u):
       if u <= 0.2:
              return 1
       if u > 0.2 and u <= 0.4:
              return 2
       if u > 0.4 and u <= 0.6:
              return 3
       if u > 0.6 and u <= 0.8:
              return 4
       if u > 0.8 and u <= 1:
              return 5
#ESTA ES LA FUNCIÓN PRINCIPAL, EL ERROR LO TOMA COMO UN FLOAT
#ASÍ QUE CUANDO PREGUNTES EL ERROR, GUARDA UNA VARIABLE CON 0.05 o 0.1
#FUNCION PRUEBAS DE SERIES
def pSeries(nums,error):
       # DICCIONARIO DE LAS DUPLAS
       duplas = {
              'n': [],
              'U1': [],
              'U2': []}
       # LISTAS PARA TRABAJAR CON LAS DUPLAS
       n=[]
       u1=[]
       u2=[]
       # DICCIONARIO PARA LA TABLA DE OBSERVADOS
       observado = {
              '--': ['1','0.8','0.6','0.4','0.2'],
              '0.2': [0]*5,
              '0.4': [0]*5,
              '0.6': [0]*5,
              '0.8': [0]*5,
              '1': [0]*5}
       # DICCIONARIO PARA LA TABLA DE ESPERADOS
       esperado = {
              '--': ['1','0.8','0.6','0.4','0.2'],
              '0.2': [(len(nums)/25)]*5,
              '0.4': [(len(nums)/25)]*5,
              '0.6': [(len(nums)/25)]*5,
              '0.8': [(len(nums)/25)]*5,
              '1': [(len(nums)/25)]*5}
       # DICCIONARIO PARA LA TABLA FINAL
       final = {
              '--': ['1','0.8','0.6','0.4','0.2'],
              '0.2': [0]*5,
              '0.4': [0]*5,
              '0.6': [0]*5,
              '0.8': [0]*5,
              '1': [0]*5}
       print('BIENVENIDO A LA PRUEBA DE SERIES')
       print('GENERANDO RESULTADOS.....')
       print('-------------------------------------------')
       #CICLO PARA GUARDAR LAS DUPLAS DE NUMEROS
       for i in range(len(nums)):
              #Mientras no sea el ultimo numero, hacer dupla con el siguiente
              if i+1<len(nums):
                     n.append(i+1)
                     u1.append(nums[i])
                     u2.append(nums[i+1])
              #Si es el ultimo numero, hacer dupla con el mismo
              else:
                     n.append(i + 1)
                     u1.append(nums[i])
                     u2.append(nums[i])
       #CICLO PARA LA TABLA DE OBSERVADO, PARA ASIGNAR EL RANGO EN EL QUE SE ENCUENTRA
       #LA FORMA EN QUE FUNCIONA ES QUE AUMENTA EL CONTEO DE ESA SECCIÓN EN 1 CUANDO ENCUENTRA UN NUMERO QUE LE PERTENECE
       for i in range(len(nums)):
              if (getCoord(u1[i]) == 1 and getCoord(u2[i]) == 1):
                     observado['0.2'][4] = observado['0.2'][4]+1
              elif (getCoord(u1[i]) == 1 and getCoord(u2[i]) == 2):
                     observado['0.2'][3] = observado['0.2'][3]+1
              elif (getCoord(u1[i]) == 1 and getCoord(u2[i]) == 3):
                     observado['0.2'][2] = observado['0.2'][2]+1
              elif (getCoord(u1[i]) == 1 and getCoord(u2[i]) == 4):
                     observado['0.2'][1] = observado['0.2'][1]+1
              elif (getCoord(u1[i]) == 1 and getCoord(u2[i]) == 5):
                     observado['0.2'][0] = observado['0.2'][0]+1
              elif (getCoord(u1[i]) == 2 and getCoord(u2[i]) == 1):
                     observado['0.4'][4] = observado['0.4'][4]+1
              elif (getCoord(u1[i]) == 2 and getCoord(u2[i]) == 2):
                     observado['0.4'][3] = observado['0.4'][3]+1
              elif (getCoord(u1[i]) == 2 and getCoord(u2[i]) == 3):
                     observado['0.4'][2] = observado['0.4'][2]+1
              elif (getCoord(u1[i]) == 2 and getCoord(u2[i]) == 4):
                     observado['0.4'][1] = observado['0.4'][1]+1
              elif (getCoord(u1[i]) == 2 and getCoord(u2[i]) == 5):
                     observado['0.4'][0] = observado['0.4'][0]+1
              elif (getCoord(u1[i]) == 3 and getCoord(u2[i]) == 1):
                     observado['0.6'][4] = observado['0.6'][4]+1
              elif (getCoord(u1[i]) == 3 and getCoord(u2[i]) == 2):
                     observado['0.6'][3] = observado['0.6'][3]+1
              elif (getCoord(u1[i]) == 3 and getCoord(u2[i]) == 3):
                     observado['0.6'][2] = observado['0.6'][2]+1
              elif (getCoord(u1[i]) == 3 and getCoord(u2[i]) == 4):
                     observado['0.6'][1] = observado['0.6'][1]+1
              elif (getCoord(u1[i]) == 3 and getCoord(u2[i]) == 5):
                     observado['0.6'][0] = observado['0.6'][0]+1
              elif (getCoord(u1[i]) == 4 and getCoord(u2[i]) == 1):
                     observado['0.8'][4] = observado['0.8'][4]+1
              elif (getCoord(u1[i]) == 4 and getCoord(u2[i]) == 2):
                     observado['0.8'][3] = observado['0.8'][3]+1
              elif (getCoord(u1[i]) == 4 and getCoord(u2[i]) == 3):
                     observado['0.8'][2] = observado['0.8'][2]+1
              elif (getCoord(u1[i]) == 4 and getCoord(u2[i]) == 4):
                     observado['0.8'][1] = observado['0.8'][1]+1
              elif (getCoord(u1[i]) == 4 and getCoord(u2[i]) == 5):
                     observado['0.8'][0] = observado['0.8'][0]+1
              elif (getCoord(u1[i]) == 5 and getCoord(u2[i]) == 1):
                     observado['1'][4] = observado['1'][4]+1
              elif (getCoord(u1[i]) == 5 and getCoord(u2[i]) == 2):
                     observado['1'][3] = observado['1'][3]+1
              elif (getCoord(u1[i]) == 5 and getCoord(u2[i]) == 3):
                     observado['1'][2] = observado['1'][2]+1
              elif (getCoord(u1[i]) == 5 and getCoord(u2[i]) == 4):
                     observado['1'][1] = observado['1'][1]+1
              elif (getCoord(u1[i]) == 5 and getCoord(u2[i]) == 5):
                     observado['1'][0] = observado['1'][0]+1
       #CICLO PARA CALCULAR (ij-Eij)²/Eij POR CASILLA Y ASIGNARLO A LA TABLA FINAL
       for i in range(5):
              final['0.2'][i] = ((math.pow((observado['0.2'][i]-esperado['0.2'][i]),2))/esperado['0.2'][i])
              final['0.4'][i] = ((math.pow((observado['0.4'][i] - esperado['0.4'][i]), 2)) / esperado['0.4'][i])
              final['0.6'][i] = ((math.pow((observado['0.6'][i] - esperado['0.6'][i]), 2)) / esperado['0.6'][i])
              final['0.8'][i] = ((math.pow((observado['0.8'][i] - esperado['0.8'][i]), 2)) / esperado['0.8'][i])
              final['1'][i] = round(((math.pow((observado['1'][i] - esperado['1'][i]), 2)) / esperado['1'][i]),5)
       #ASIGNACIÓN DE LISTAS DE DUPLAS A SUS DICCIONARIOS
       duplas['n']=n
       duplas['U1']=u1
       duplas['U2']=u2
       #IMPRESIÓN DE TABLAS
       print('TABLA DE DUPLAS')
       print(tabulate(duplas, headers='keys', tablefmt='fancy_grid'))
       print('-------------------------------------------')
       print('Observado Oij')
       print(tabulate(observado, headers='keys', tablefmt='fancy_grid'))
       print('-------------------------------------------')
       print('Esperado Eij')
       print(tabulate(esperado, headers='keys', tablefmt='fancy_grid'))
       print('-------------------------------------------')
       print('TABLA FINAL (ij-Eij)²/Eij')
       print(tabulate(final, headers='keys', tablefmt='fancy_grid'))
       #INICIALIZACIÓN DE Xo²
       xo=0
       #SUMATORIA DE TODOS LOS OBSERVADOS
       for i in range(5):
              xo=xo+final['0.2'][i]+final['0.4'][i]+final['0.6'][i]+final['0.8'][i]+final['1'][i]
       print('-------------------------------------------')
       print('CONCLUSIONES FINALES')
       #CONDICIONES PARA LAS CONCLUSIONES FINALES
       #SI Xo² <= Xn²-¹,% error
       if xo <= round(sct.chi2.ppf(1-error,24),4):
              print('Xo² =',xo)
              print('Xn²-¹,'+str(int((error*100)))+"% =",round(sct.chi2.ppf(1-error,24),4))
              print(xo,'<=',round(sct.chi2.ppf(1-error,24),4))
              print('Por lo tanto los numeros si son independientes')
       #SI Xo² >= Xn²-¹,% error
       else:
              print('Xo² =',xo)
              print('Xn²-¹,'+str(int((error*100)))+"% =",round(sct.chi2.ppf(1-error,24),4))
              print(xo,'>=', round(sct.chi2.ppf(1 - error, 24), 4))
              print('Por lo tanto los numeros no son independientes')
       #CREACIÓN DE LA GRAFICA DE PUNTOS
       plt.grid()
       #IMPRESIÓN DE LOS PUNTOS EN EL GRAFICO
       for i in range(len(nums)):
              plt.plot(u1[i],u2[i],marker='.',color="b")
       plt.title('Grafico de puntos - Prueba de series')
       plt.show()
#FUNCION PRUEBA DE LAS DISTANCIAS
def pDistancias(nums,error,a,b):
       # DICCIONARIO DE LAS DISTANCIAS
       dist = {
              'n': [],
              'Ui': [],
              'E': [],
              'i': []}
       # LISTAS PARA TRABAJAR CON LAS DISTANCIAS
       # DICCIONARIO PARA LA TABLA FINAL
       final = {
              'i': [],
              'Pi': [],
              'Oi': [],
              'Ei': [],
              'Oi-Ei': [],
              '(Oi-Ei)²/Ei': []}
       rep = {
              '0': [0],
              '1': [0],
              '2': [0],
              '3': [0],
              '4': [0],
              '5': [0],
              '-': [0]}
       print('BIENVENIDO A LA PRUEBA DE DISTANCIAS O HUECOS')
       print('GENERANDO RESULTADOS.....')
       print('-------------------------------------------')
       # CICLO PARA GUARDAR LAS DISNTACIAS DE LOS NUMEROS
       cZero = 0
       cOne = 0
       for i in range(len(nums)):
              if nums[i]<a or nums[i]>b:
                     if cOne==0:
                            rep['0'][0] = rep['0'][0] + 1
                     elif cOne==1:
                            rep['1'][0] = rep['1'][0] + 1
                     elif cOne == 2:
                            rep['2'][0] = rep['2'][0] + 1
                     elif cOne == 3:
                            rep['3'][0] = rep['3'][0] + 1
                     elif cOne == 4:
                            rep['4'][0] = rep['4'][0] + 1
                     elif cOne == 5:
                            rep['5'][0] = rep['5'][0] + 1
                     else:
                            rep['-'][0] = rep['-'][0] + 1
                     cOne=0
                     cZero=cZero+1
                     dist['n'].append(i+1)
                     dist['Ui'].append(nums[i])
                     dist['E'].append(0)
                     dist['i'].append(cZero)
              elif nums[i]>=a and nums[i]<=b:
                     if cZero == 0:
                            rep['0'][0]=rep['0'][0] + 1
                     elif cZero == 1:
                            rep['1'][0] = rep['1'][0] + 1
                     elif cZero == 2:
                            rep['2'][0] = rep['2'][0] + 1
                     elif cZero == 3:
                            rep['3'][0] = rep['3'][0] + 1
                     elif cZero == 4:
                            rep['4'][0] = rep['4'][0] + 1
                     elif cZero == 5:
                            rep['5'][0] = rep['5'][0] + 1
                     else:
                            rep['-'][0] = rep['-'][0] + 1
                     cZero=0
                     cOne = cOne + 1
                     dist['n'].append(i + 1)
                     dist['Ui'].append(nums[i])
                     dist['E'].append(1)
                     dist['i'].append(0)
       finales=0
       for i in range(7):
              if rep[list(rep.keys())[i]][0] == 0:
                     maximun=i
                     break;
       for i in range(7-maximun):
              finales=finales+rep[list(rep.keys())[i+maximun]][0]
       total = 0
       for i in range(7):
              total=total+rep[list(rep.keys())[i]][0]
       eTotal=0
       for i in range(maximun):
              if i == 0:
                     final['i'].append(str(i))
                     final['Pi'].append(b-a)
                     final['Oi'].append(rep[list(rep.keys())[i]][0])
                     final['Ei'].append(total*(final['Pi'][i]))
                     final['Oi-Ei'].append((final['Oi'][i])-(final['Ei'][i]))
                     final['(Oi-Ei)²/Ei'].append(math.pow(final['Oi-Ei'][i],2)/(final['Ei'][i]))
                     eTotal=eTotal+final['(Oi-Ei)²/Ei'][i]
              elif i > 0 and i < maximun-1:
                     final['i'].append(str(i))
                     final['Pi'].append((math.pow((1-(b-a)),i))*(b-a))
                     final['Oi'].append(rep[list(rep.keys())[i]][0])
                     final['Ei'].append(total * (final['Pi'][i]))
                     final['Oi-Ei'].append((final['Oi'][i]) - (final['Ei'][i]))
                     final['(Oi-Ei)²/Ei'].append(math.pow(final['Oi-Ei'][i], 2) / (final['Ei'][i]))
                     eTotal = eTotal + final['(Oi-Ei)²/Ei'][i]
              elif i == maximun-1:
                     final['i'].append('>='+str(i))
                     final['Pi'].append(math.pow((1 - (b - a)), i))
                     final['Oi'].append((rep[list(rep.keys())[i]][0])+finales)
                     final['Ei'].append(total * (final['Pi'][i]))
                     final['Oi-Ei'].append((final['Oi'][i]) - (final['Ei'][i]))
                     final['(Oi-Ei)²/Ei'].append(math.pow(final['Oi-Ei'][i], 2) / (final['Ei'][i]))
                     eTotal = eTotal + final['(Oi-Ei)²/Ei'][i]
       final['i'].append('Total')
       final['Pi'].append(1)
       final['Oi'].append(total)
       final['Ei'].append(total)
       final['Oi-Ei'].append('E=')
       final['(Oi-Ei)²/Ei'].append(eTotal)
       print('TABLA DISTANCIAS')
       print(tabulate(dist, headers='keys', tablefmt='fancy_grid'))
       print('-------------------------------------------')
       print('TABLA FINAL (Oi-Ei)²/Ei')
       print(tabulate(final, headers='keys', tablefmt='fancy_grid'))
       # INICIALIZACIÓN DE Xo²
       xo = eTotal
       print('-------------------------------------------')
       print('CONCLUSIONES FINALES')
       # CONDICIONES PARA LAS CONCLUSIONES FINALES
       # SI Xo² <= Xn²-¹,% error
       if xo <= round(sct.chi2.ppf(1 - error, len(nums)), 4):
              print('Xo² =', xo)
              print('Xn²-¹,' + str(int((error * 100))) + "% =", round(sct.chi2.ppf(1 - error, len(nums)), 4))
              print(xo, '<=', round(sct.chi2.ppf(1 - error, len(nums)), 4))
              print('Por lo tanto los numeros si son independientes')
       # SI Xo² >= Xn²-¹,% error
       else:
              print('Xo² =', xo)
              print('Xn²-¹,' + str(int((error * 100))) + "% =", round(sct.chi2.ppf(1 - error, len(nums)), 4))
              print(xo, '>=', round(sct.chi2.ppf(1 - error, len(nums)), 4))
              print('Por lo tanto los numeros no son independientes')

def quintilla(numero):
       long=len(str(numero))
       numero=(str(numero))[2:long-1]
       digito1 = numero[0]
       for digito in numero:
              if digito != digito1:
                     return False
       return True
def full(numero):
       # Conteo
       long=len(str(numero))
       numero = (str(numero))[2:long - 1]
       guia = dict.fromkeys(numero, 0)
       for digito in numero:
              guia[digito]+=1
       if(2 in guia.values() and 3 in guia.values()):
              return True
       return False
def pokerF(numero):
       long=len(str(numero))
       numero = int((str(numero))[2:long - 1])
       if(tercia(numero)):
              # Conteo
              guia = dict.fromkeys(numero, 0)
              for digito in numero:
                     guia[digito]+=1
              for conteo in guia.values():
                     if conteo >= 4:
                            return True
              return False
       else:
              return False
def tercia(numero):
       long=len(str(numero))
       numero = (str(numero))[2:long - 1]
       # Conteo
       guia = dict.fromkeys(numero, 0)
       for digito in numero:
              guia[digito]+=1
       # Impar
       for conteo in guia.values():
              if conteo >= 3:
                     return True
       return False
def unPar(numero):
       long=len(str(numero))
       numero = (str(numero))[2:long - 1]
       # Conteo
       guia = dict.fromkeys(numero, 0)
       for digito in numero:
              guia[digito]+=1
       # Par
       for conteo in guia.values():
              if conteo >= 2:
                     return True
       return False
def dosPares(numero):
       long=len(str(numero))
       numero = (str(numero))[2:long - 1]
       # Conteo
       guia = dict.fromkeys(numero, 0)
       for digito in numero:
              guia[digito]+=1
       # Primer par
       # Solo si sabemos que había uno
       if unPar(numero):
              par = None
              for conteo in guia.items():
                     if conteo[1] >= 2:
                            par = conteo[0]
                            break;
              # Quitamos el que había
              del guia[par]
              # Segundo par
              for conteo in guia.values():
                     if conteo >= 2:
                            return True
              return False
       else:
              return False
def pachuca(numero):
       long=len(str(numero))
       numero = (str(numero))[2:long - 1]
       return not (len(numero) != len(set(numero)))

def pPoker(nums,error):
       # DICCIONARIO DE POKER
       poker = {
              'n': [],
              'Ri': [],
              'Evento': []}
       # DICCIONARIO PARA LA TABLA FINAL
       final = {
              'Evento': ['Pachuca','1 Par','Tercia','2 Pares','Full','Poker','Quintilla'],
              'FO': [],
              'PE': [0.3024,0.5040,0.0720,0.1080,0.0090,0.0045,0.0001],
              'FE': [],
              '(FO-FE)²/FE': []}
       rep = {
              'Pachuca': [0],
              '1 Par': [0],
              'Tercia': [0],
              '2 Pares': [0],
              'Full': [0],
              'Poker': [0],
              'Quintilla': [0]}
       print('BIENVENIDO A LA PRUEBA DE POKER')
       print('GENERANDO RESULTADOS.....')
       print('-------------------------------------------')
       for i in range(len(nums)):
              poker['n'].append(i+1)
              poker['Ri'].append(nums[i])
              if quintilla(nums[i]):
                     poker['Evento'].append('Quintilla')
                     rep['Quintilla'][0]=rep['Quintilla'][0]+1
              elif pokerF(nums[i]):
                     poker['Evento'].append('Poker')
                     rep['Poker'][0] = rep['Poker'][0] + 1
              elif full(nums[i]):
                     poker['Evento'].append('Full')
                     rep['Full'][0] = rep['Full'][0] + 1
              elif tercia(nums[i]):
                     poker['Evento'].append('Tercia')
                     rep['Tercia'][0] = rep['Tercia'][0] + 1
              elif dosPares(nums[i]):
                     poker['Evento'].append('2 Pares')
                     rep['2 Pares'][0] = rep['2 Pares'][0] + 1
              elif unPar(nums[i]):
                     poker['Evento'].append('1 Par')
                     rep['1 Par'][0] = rep['1 Par'][0] + 1
              else:
                     poker['Evento'].append('Pachuca')
                     rep['Pachuca'][0] = rep['Pachuca'][0] + 1
       total=0
       for i in range(7):
              final['FO'].append(rep[list(rep.keys())[i]][0])
              final['FE'].append(len(nums)*(final['PE'][i]))
              final['(FO-FE)²/FE'].append((math.pow((final['FO'][i]-final['FE'][i]),2))/final['FE'][i])
              total=total+(math.pow((final['FO'][i]-final['FE'][i]),2))/final['FE'][i]
       final['Evento'].append('Totales=')
       final['FO'].append(len(nums))
       final['PE'].append(1)
       final['FE'].append(1)
       final['(FO-FE)²/FE'].append(total)
       print('TABLA POKER')
       print(tabulate(poker, headers='keys', tablefmt='fancy_grid'))
       print('-------------------------------------------')
       print('TABLA FINAL (FO-FE)²/FE')
       print(tabulate(final, headers='keys', tablefmt='fancy_grid'))
       # INICIALIZACIÓN DE Xo²
       xo = total
       print('-------------------------------------------')
       print('CONCLUSIONES FINALES')
       # CONDICIONES PARA LAS CONCLUSIONES FINALES
       # SI Xo² <= Xn²-¹,% error
       if xo <= round(sct.chi2.ppf(1 - error, 6), 4):
              print('Xo² =', xo)
              print('X6²,' + str(int((error * 100))) + "% =", round(sct.chi2.ppf(1 - error, 6), 4))
              print(xo, '<=', round(sct.chi2.ppf(1 - error, 6), 4))
              print('Por lo tanto los numeros si son independientes')
       # SI Xo² >= Xn²-¹,% error
       else:
              print('Xo² =', xo)
              print('X6²,' + str(int((error * 100))) + "% =", round(sct.chi2.ppf(1 - error, 6), 4))
              print(xo, '>=', round(sct.chi2.ppf(1 - error, 6), 4))
              print('Por lo tanto los numeros no son independientes')

#pPoker(nums,0.05)
#pSeries(nums,0.05)
#pDistancias(nums,0.05,0.3,0.6)
