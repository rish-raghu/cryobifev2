# activate cryodrgn env first!

import argparse
import os
import subprocess, shlex
import pandas as pd 

parser = argparse.ArgumentParser(description= \
"Generate cryo-em images from volumes according to their boltzmann distribution")
parser.add_argument('voldir', help='directory containing volumes')
parser.add_argument('fe', help='csv file containing normalized probability of each volume')
parser.add_argument('N', type=int, help="total number of images to generate")
parser.add_argument('-o', required=True, help='directory to store images')
args = parser.parse_args()

os.makedirs(args.o, exist_ok=True)
prob = pd.read_csv(args.fe)['probnorm'].tolist()
for i in range(len(prob)):
    cmd = f"python /scratch/gpfs/rraghu/cryosim/project3d.py \
        {os.path.join(args.voldir, f'volume_{i+1}.mrc')} \
        --out-pose {os.path.join(args.o, f'poses_{i+1}.pkl')} \
        -o {os.path.join(args.o, f'images_{i+1}.mrcs')} \
        -N {int(round(prob[i]*args.N))} --t-extent 0"
    subprocess.run(shlex.split(cmd))

pose_files = [os.path.join(args.o, f'poses_{i+1}.pkl') for i in range(len(prob))]
subprocess.run(shlex.split(f"cryodrgn_utils concat_pkls {' '.join(pose_files)} \
    -o {os.path.join(args.o, 'poses.pkl')}"))
