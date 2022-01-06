import numpy as np


def derivative(y, x):
    return (y[1:] - y[:-1])/(x[1] - x[0])


def integral(y, x):
    return np.cumsum(((y[1:] + y[:-1]))*(x[1]-x[0])/2)
