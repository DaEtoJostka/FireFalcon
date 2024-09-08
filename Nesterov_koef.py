import numpy as np
import pandas as pd

"""Коэффециент пожароопасности
в лесу по условиям погоды определяется на 12…14 ч местного времени, 
как сумма произведения температуры воздуха на разность температур 
воздуха и точки росы за (n) дней без дождя

temp: массив температур за последние n дней
dew: точка россы за последние n дней
precip: количество мм осадков за последние n дней
"""
def CFD(temp: np.array, dew: np.array, precip: np.array):
    coef = [temp[0] * (temp[0] - dew[0])]
    for i in range(1, len(temp)):
        if precip[i] > 3:
            coef.append(0)
        else:
            coef.append(coef[i-1] + temp[i] * (temp[i] - dew[i]))

    return coef
    