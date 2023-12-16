#!/bin/bash

#SBATCH -p cryoem
#SBATCH -t 2:00:00
#SBATCH --mem=64G
#SBATCH --gres=gpu:1
#SBATCH -J bioem

for i in {1..20}
do  
    ../BioEM/bioEM --Inputfile bioem/CONFIG_TUT --Modelfile rotated_pdbs/angle_$i.pdb --ReadPDB --Particlesfile images/ctf/subset10_11.mrcs --ReadMRC --ReadOrientation ../BioEM/Quaternions/QUATERNION_LIST_4608_Orient --OutputFile bioem/ctf_sub11_med_v2/prob_$i
done
