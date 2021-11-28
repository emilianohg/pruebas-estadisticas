import pandas as pd
from scipy import stats

def ks_critical_value(n_trials, alpha):
    return stats.ksone.ppf(1-alpha/2, n_trials)

def kolmogorov(numeros_aleatorios, porcentaje):

    print('=== PRUEBA DE KOLMOGOROV ===')

    N = len(numeros_aleatorios)
    numeros_aleatorios_ordenados = sorted(numeros_aleatorios)

    tabla = pd.DataFrame(columns=[
        'i',
        'Ui',
        'i/N',
        'Di',
    ])

    for i in range(1, N + 1):
        Ui = numeros_aleatorios_ordenados[i - 1]
        data = {
            'i': i,
            'Ui': Ui,
            'i/N': i / N,
            'Di': abs(Ui - (i / N)),
        }

        tabla = tabla.append(data, ignore_index=True)

    print('')
    print('=== TABLA ===')
    print(tabla)

    print('')
    print('=== VALOR MAYOR ===')

    max = tabla[tabla.Di == tabla.Di.max()]
    print(max)

    Dk = ks_critical_value(N, porcentaje)
    Di = tabla.Di.max()

    print('')
    print('=== RESULTADO ===')
    print('Los números están uniformemente distribuidos' if Di <= Dk else 'Los números NO están uniformemente distribuidos')