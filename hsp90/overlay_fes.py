import os
import numpy as np
from scipy.interpolate import UnivariateSpline
import pandas as pd
import matplotlib.pyplot as plt

fesSmall = np.load('bioem/ctf_all_small_v2/mcfes.npy')
avgFesSmall = np.mean(fesSmall[1000:, :], axis=0)
fesMed = np.load('bioem/ctf_all_med_v2/mcfes.npy')
avgFesMed = np.mean(fesMed[1000:, :], axis=0)
fesLarge = np.load('bioem/ctf_all_large_v2/mcfes.npy')
avgFesLarge = np.mean(fesLarge[1000:, :], axis=0)

cv = np.linspace(0, 1, 20)
splineFuncSmall = UnivariateSpline(cv, avgFesSmall)
splineFuncMed = UnivariateSpline(cv, avgFesMed)
splineFuncLarge = UnivariateSpline(cv, avgFesLarge)
splineFuncTrue = lambda x: -np.log(np.exp(-(19*x-6)**2 / 8) + np.exp(-(19*x-15)**2 / 18)/3)

cv = np.linspace(0, 1, 100)
splineSmall = splineFuncSmall(cv)
splineSmall -= np.min(splineSmall)
splineMed = splineFuncMed(cv)
splineMed -= np.min(splineMed)
splineLarge = splineFuncLarge(cv)
splineLarge -= np.min(splineLarge)
splineTrue = splineFuncTrue(cv)
splineTrue -= np.min(splineTrue)

plt.plot(cv, splineTrue, color='black', label="True")
plt.plot(cv, splineSmall, color='green', label="CryoBIFE - 0.5k orientations")
plt.plot(cv, splineMed, color='red', label="CryoBIFE - 4k orientations")
plt.plot(cv, splineLarge, color='blue', label="CryoBIFE - 36k orientations")
plt.xlabel("Path CV")
plt.ylabel("Free energy")
plt.legend()
plt.savefig('allfes.png')
