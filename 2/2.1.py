import numpy as np
m = 1000
n = 250
l = 100

def gn(en):
    num = 0
    for i in range(en):
        num = num + np.random.uniform(0,1) - 0.5
    return np.sqrt(12/en)*num

def gn1():
    return np.sqrt(-2 * np.log(np.random.uniform(0,1)))*np.cos(2*np.pi*np.random.uniform(0,1))

def gn2():
    return np.sqrt(-2 * np.log(np.random.uniform(0,1)))*np.sin(2*np.pi*np.random.uniform(0,1))

eps = 0
