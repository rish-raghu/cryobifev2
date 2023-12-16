import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path_cv = np.linspace(0.0, 1.0, num=20)
prob = np.exp(-(19*path_cv-6)**2 / 8) + np.exp(-(19*path_cv-15)**2 / 18)/3
prob_norm = prob/np.sum(prob)
fe = -np.log(prob)

df = pd.DataFrame({'pathcv': path_cv, 'fe': fe, 'prob': prob, 'probnorm': prob_norm})
df.to_csv("true.csv", index=False)

# plt.plot(path_cv, fe)
# plt.savefig("fes.png")
