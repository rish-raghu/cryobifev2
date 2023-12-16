import argparse
import os
import numpy as np
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Plot average FES across MC timesteps")
parser.add_argument('dir', help='directory containing .npy file with FES estimates')
parser.add_argument('M', type=int, help='number of models')
parser.add_argument('--start', type=int, default=0, help="timestep to start averaging on")
args = parser.parse_args()

fes = np.load(os.path.join(args.dir, 'mcfes.npy'))
avgFes = np.mean(fes[args.start:, :], axis=0)
cv = np.linspace(0, 1, args.M)

plt.plot(cv, avgFes)
plt.xlabel("Path CV")
plt.ylabel("Free energy")
plt.savefig(os.path.join(args.dir, 'mcfes.png'))
plt.clf()

spline = UnivariateSpline(cv, avgFes)
x = np.linspace(0, 1, 100)
plt.plot(x, spline(x))
plt.xlabel("Path CV")
plt.ylabel("Free energy")
plt.savefig(os.path.join(args.dir, 'mcfes_spline.png'))
