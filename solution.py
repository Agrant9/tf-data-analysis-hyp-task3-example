import pandas as pd
import numpy as np
from scipy.stats import ks_2samp


chat_id = 544835691 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    stat, pval = ks_2samp(x, y, alternative='greater')
    return True if pval < 0.07 else False # Ваш ответ, True или False
