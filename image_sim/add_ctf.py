import argparse
import os
import glob
import subprocess, shlex

parser = argparse.ArgumentParser(description= "Add ctf to projection image stacks")
parser.add_argument('imagedir', help='directory containing image stacks')
parser.add_argument('apix', help='pixel size')
parser.add_argument('--df-std', default=0, type=float, help='stddev for defocus')
parser.add_argument('-o', required=True, help='directory to store images')
args = parser.parse_args()

num_files = len(glob.glob(os.path.join(args.imagedir, 'images_*.mrcs')))
os.makedirs(args.o, exist_ok=True)
for i in range(num_files):
    cmd = f"python /scratch/gpfs/rraghu/cryosim/add_ctf.py \
        {os.path.join(args.imagedir, f'images_{i+1}.mrcs')} \
        --out-pkl {os.path.join(args.o, f'ctf_{i+1}.pkl')} \
        -o {os.path.join(args.o, f'images_{i+1}.mrcs')} \
        --Apix {args.apix} --sample-df {args.df_std} \
        --s1 0 --s2 0"
    subprocess.run(shlex.split(cmd))

ctf_files = [os.path.join(args.o, f'ctf_{i+1}.pkl') for i in range(num_files)]
subprocess.run(shlex.split(f"cryodrgn_utils concat_pkls {' '.join(ctf_files)} \
    -o {os.path.join(args.o, 'ctf.pkl')}"))
