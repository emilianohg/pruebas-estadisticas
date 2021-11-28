import math
from random import random

from Pruebas import pSeries, pDistancias, pPoker
from chi_cuadrado import chi_cuadrado
from kolmogorov import kolmogorov

print("=== EVALUACIÓN DE PRUEBAS ESTADÍSTICAS ===")


def get_total_numeros():
    while (True):
        n = int(input("Ingresa el total de numeros a generar: "))
        if n < 34:
            print('El total de numeros generados debe ser mayor o igual a 34')
        else:
            break

    return n


def generar_numeros(total_numeros):
    numeros_aleatorios = []

    for i in range(total_numeros):
        numero = random()
        numero_trunc = math.trunc(numero * 100000) / float(100000)
        numeros_aleatorios.append(numero_trunc)

    return numeros_aleatorios


def seleccionar_prueba(numeros_aleatorios):
    while True:
        print('')
        print('¿Qué prueba quieres aplicar?')
        print('')
        print('1. Chi2')
        print('2. Kolmogorov')
        print('3. Series')
        print('4. Distancias o Huecos')
        print('5. Poker')
        print('6. Salir')
        print('')

        opcion = int(input('Selecciona una opción: '))

        if opcion == 6:
            print('BYE!')
            break

        if opcion not in range(1, 6):
            print('¡Selecciona una opción valida!')
            continue

        porcentaje = seleccionar_porcentaje_fallo()

        if opcion == 1:
            chi_cuadrado(numeros_aleatorios, porcentaje)
        elif opcion == 2:
            kolmogorov(numeros_aleatorios, porcentaje)
        elif opcion == 3:
            pSeries(numeros_aleatorios, porcentaje)
        elif opcion == 4:
            pDistancias(numeros_aleatorios, porcentaje, 0.3, 0.6)
        elif opcion == 5:
            pPoker(numeros_aleatorios, porcentaje)


def seleccionar_porcentaje_fallo():
    while True:
        print('')
        print('¿Qué porcentaje de fallo quieres aplicar?')
        print('')
        print('1. 5%')
        print('2. 10%')
        print('')

        opcion = int(input('Selecciona una opción: '))

        if opcion == 1:
            return 0.05
        elif opcion == 2:
            return 0.1
        else:
            print('¡Selecciona una opción valida!')


total_numeros = get_total_numeros()
numeros_aleatorios = generar_numeros(total_numeros)
seleccionar_prueba(numeros_aleatorios)
