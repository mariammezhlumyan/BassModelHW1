import numpy as np 


def bass_model(t, p, q, M):
    return (M * ((p + q)**2 / p) * np.exp(-(p + q) * t)) / (1 + (q / p) * np.exp(-(p + q) * t))**2