import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('empot.xvg', sep='\s+', header=None, names=['step','energy'])
df.plot('step', legend=None)
plt.xlabel("Time step")
plt.ylabel("Potential energy")
plt.title("Energy minimization")
plt.tight_layout()
plt.savefig('empot.png')
