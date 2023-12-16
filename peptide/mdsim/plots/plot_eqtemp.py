import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('eqtemp.xvg', sep='\s+', header=None, names=['time','temperature'])
df.plot('time', legend=None)
plt.xlabel("Time (ps)")
plt.ylabel("Temperature (K)")
plt.title("NVT Equilibration")
plt.tight_layout()
plt.savefig('eqtemp.png')
