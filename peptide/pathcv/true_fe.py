import numpy as np 
import matplotlib.pyplot as plt 
from scipy.interpolate import UnivariateSpline
import pandas as pd

cvs = np.load('path_cvs.npy')
counts = plt.hist(cvs, bins=10)
plt.savefig("cv_hist.png")
plt.clf()

prob = counts[0]/np.sum(counts[0])
fe = -np.log(prob)
#splineFunc = UnivariateSpline(np.linspace(0, 1, 10), fe)
#spline = splineFunc(np.linspace(0, 1, 100))
#plt.plot(np.linspace(0, 1, 100), spline)
cv = np.linspace(0, 1, 10)
plt.plot(cv, fe)
plt.savefig("true_fe.png")

df = pd.DataFrame({'pathcv': cv, 'fe': fe, 'prob': prob, 'probnorm': prob})
df.to_csv("true.csv", index=False)

# nodes = np.load('node_idxs.npy')
# print(cvs[nodes])
