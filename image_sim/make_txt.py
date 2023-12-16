import argparse
import glob
import os

parser = argparse.ArgumentParser(description="Make .txt file of .mrcs files")
parser.add_argument('stackdir', help='directory containing image stacks')
parser.add_argument('-o', required=True, help='output filename')
args = parser.parse_args()

files = glob.glob(os.path.join(args.stackdir, 'images_*.mrcs'))
files = [os.path.basename(file) for file in files]
files = sorted(files, key=lambda file: int(file.replace('_', '.').split('.')[1]))

f = open(args.o, 'w')
for file in files:
    f.write(file + '\n')
f.close()
