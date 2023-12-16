import argparse
import os
import glob
import subprocess, shlex

parser = argparse.ArgumentParser(description= "Add noise to projection image stacks")
parser.add_argument('imagedir', help='directory containing image stacks')
parser.add_argument('snr', help='signal-to-noise ratio')
parser.add_argument('-o', required=True, help='directory to store images')
args = parser.parse_args()

num_files = len(glob.glob(os.path.join(args.imagedir, 'images_*.mrcs')))
os.makedirs(args.o, exist_ok=True)
for i in range(num_files):
    cmd = f"python /scratch/gpfs/rraghu/cryosim/add_noise.py \
        {os.path.join(args.imagedir, f'images_{i+1}.mrcs')} \
        -o {os.path.join(args.o, f'images_{i+1}.mrcs')} \
        --snr {args.snr}"
    subprocess.run(shlex.split(cmd))
