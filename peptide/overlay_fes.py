import os
import numpy as np
from scipy.interpolate import UnivariateSpline
import pandas as pd
import matplotlib.pyplot as plt

fesMed = np.load('bioem/raw_all_med/mcfes.npy')
avgFesMed = np.mean(fesMed[1000:, :], axis=0)
avgFesMed -= np.min(avgFesMed)
fesLarge = np.load('bioem/raw_all_large/mcfes.npy')
avgFesLarge = np.mean(fesLarge[1000:, :], axis=0)
avgFesLarge -= np.min(avgFesLarge)

cvs = np.load('pathcv/path_cvs.npy')
counts = plt.hist(cvs, bins=10)
plt.clf()
prob = counts[0]/np.sum(counts[0])
fe = -np.log(prob)
fe -= np.min(fe)

cv = np.linspace(0, 1, 10)
plt.plot(cv, fe, color='black', label='True')
plt.plot(cv, avgFesMed, color='red', label="CryoBIFE - 4k orientations")
plt.plot(cv, avgFesLarge, color='blue', label="CryoBIFE - 36k orientations")
plt.xlabel("Path CV")
plt.ylabel("Free energy")
plt.legend()
plt.savefig('allfes.png')
