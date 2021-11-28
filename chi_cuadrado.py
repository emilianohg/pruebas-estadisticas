import math
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np


def grafica_barra(axis_x, axis_y, esperado):
    data = axis_y
    labels = ["{:10.5f}".format(x) for x in axis_x]
    plt.xticks(range(len(data)), labels)
    plt.xlabel('Rangos')
    plt.ylabel('Valor')
    plt.title('Chi cuadrado')
    plt.bar(range(len(data)), data)
    plt.axhline(y=esperado, color='r', linestyle='-')

    plt.show()

def chi_cuadrado(numeros_aleatorios, porcentaje):
    N = len(numeros_aleatorios)
    print('=== PRUBEBA CHI CUADRADO ===')

    # numero de intervalos
    k = math.ceil(math.sqrt(N))

    # numeros_por_intervalo
    E = N / k

    rango_intervalo = 1 / k

    tabla = pd.DataFrame(columns=[
        'limite_inferior',
        'limite_superior',
        'O',
        'E',
        'O - E',
        '(O - E)^2 / E'
    ])

    for i in range(k):
        numeros_intervalo = list(
            filter(lambda n: n >= (i * rango_intervalo) and n < ((i + 1) * rango_intervalo), numeros_aleatorios))

        O = len(numeros_intervalo)

        data = {
            'limite_inferior': i * rango_intervalo,
            'limite_superior': (i + 1) * rango_intervalo,
            'O': O,
            'E': E,
            'O - E': O - E,
            '(O - E)^2 / E': math.pow(O - E, 2) / E
        }

        tabla = tabla.append(data, ignore_index=True)

    chi_cuadrado = tabla['(O - E)^2 / E'].sum()

    prob = 1 - porcentaje
    chi_cuadrado_tabla = stats.chi2.ppf(prob, k - 1)

    print('')
    print('=== TABLA ===')

    print(tabla)

    print('')
    print('=== GRAFICA ===')

    grafica_barra(tabla['limite_superior'].tolist(), tabla['O'].tolist(), E)

    print('')
    print('chi cuadrado =', chi_cuadrado)
    print('chi cuadrado de tabla =', chi_cuadrado_tabla)
    print('')
    print('=== RESULTADO ===')
    print('Los números estan uniformemente distribuidos' if chi_cuadrado <= chi_cuadrado_tabla else 'Los números NO estan uniformemente distribuidos')