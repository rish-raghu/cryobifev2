import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('eqdensity.xvg', sep='\s+', header=None, names=['time','density'])
df.plot('time', legend=None)
plt.xlabel("Time (ps)")
plt.ylabel("Density (kg/m^3)")
plt.title("NPT Equilibration")
plt.tight_layout()
plt.savefig('eqdensity.png')
