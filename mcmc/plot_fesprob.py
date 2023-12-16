import argparse
import os
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Plot log probability of FES across MC timesteps")
parser.add_argument('dir', help='directory containing .npy file with log probabilities')
parser.add_argument('--start', type=int, default=0, help="timestep to start plot on")
args = parser.parse_args()

probs = np.load(os.path.join(args.dir, 'mcfesprob.npy'))
plt.plot(probs[args.start:])
plt.xlabel("MC Step")
plt.ylabel("Log probability of FES")
plt.savefig(os.path.join(args.dir, 'mcfesprob.png'))
