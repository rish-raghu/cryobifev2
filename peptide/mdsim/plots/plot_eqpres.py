import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('eqpres.xvg', sep='\s+', header=None, names=['time','pressure'])
df.plot('time', legend=None)
plt.xlabel("Time (ps)")
plt.ylabel("Pressure (atm)")
plt.title("NPT Equilibration")
plt.tight_layout()
plt.savefig('eqpres.png')
