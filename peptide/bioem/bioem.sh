#!/bin/bash

for i in {1..10}
do 
    sbatch -p cryoem -t 1:00:00 --mem=64G --gres=gpu:1 -n 2 -J bioem --wrap "../../BioEM/bioEM --Inputfile CONFIG --Modelfile pdbs/conf_$i.pdb --ReadPDB --Particlesfile ../image_sim2/raw.mrcs --ReadMRC --ReadOrientation ../../BioEM/Quaternions/QUATERNION_LIST_36864_Orient --OutputFile raw_all_large/prob_$i"
done
