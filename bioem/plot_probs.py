import argparse
import os
import glob
import numpy as np 
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Plot probability of images being generated from models")
parser.add_argument('bioemdir', help='directory containing bioem outputs')
parser.add_argument('N', type=int, help='number of images')
args = parser.parse_args()

files = glob.glob(os.path.join(args.bioemdir, 'prob_*'))
files = [os.path.basename(file) for file in files]
files = sorted(files, key=lambda file: int(file.replace('_', '.').split('.')[1]))

probs = np.zeros((len(files), args.N))
for modelNum, file in enumerate(files):
    f = open(os.path.join(args.bioemdir, file), 'r')
    for _ in range(5): f.readline()
    for imageNum in range(args.N):
        probs[modelNum, imageNum] = f.readline().split()[3]
        f.readline()
    f.close()

plt.plot(np.arange(1, len(files)+1), probs)
plt.xlabel("Model number")
plt.xticks(np.arange(1, len(files)+1))
plt.ylabel("Log probability of image")
plt.tight_layout()
plt.savefig(os.path.join(args.bioemdir, 'plot.png'))
