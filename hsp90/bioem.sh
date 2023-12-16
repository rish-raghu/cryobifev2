#!/bin/bash

for i in {1..20}
do 
    sbatch -p cryoem -t 1:00:00 --mem=64G --gres=gpu:1 -n 1 -J bioem --wrap "../BioEM/bioEM --Inputfile bioem/CONFIG --Modelfile rotated_pdbs/angle_$i.pdb --ReadPDB --Particlesfile images/ctf/images.mrcs --ReadMRC --ReadOrientation ../BioEM/Quaternions/QUATERNION_LIST_576_Orient --OutputFile bioem/ctf_all_small_v2/prob_$i"
done
