import numpy as np

def calculate(numeros):
    if len(numeros) != 9:
        raise ValueError("A lista tem que conter nove números!")

    matriz = np.array(numeros).reshape(3, 3)

    calculos = {
        'mean': [
            matriz.mean(axis=0).tolist(),
            matriz.mean(axis=1).tolist(),
            matriz.flatten().mean()
        ],
        'variance': [
            matriz.var(axis=0).tolist(),
            matriz.var(axis=1).tolist(),
            matriz.flatten().var()
        ],
        'standard deviation': [
            matriz.std(axis=0).tolist(),
            matriz.std(axis=1).tolist(),
            matriz.flatten().std()
        ],
        'max': [
            matriz.max(axis=0).tolist(),
            matriz.max(axis=1).tolist(),
            matriz.flatten().max()
        ],
        'min': [
            matriz.min(axis=0).tolist(),
            matriz.min(axis=1).tolist(),
            matriz.flatten().min()
        ],
        'sum': [
            matriz.sum(axis=0).tolist(),
            matriz.sum(axis=1).tolist(),
            matriz.flatten().sum()
        ]
    }
    return calculos