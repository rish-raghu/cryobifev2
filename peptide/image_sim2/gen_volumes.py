from chimerax.core.commands import run
import os

run(session, 'open ../mdsim/peptide_box.gro')
run(session, 'open ../mdsim/prod_align.xtc')

for i in range(1, 10002):
    run(session, f'coordset #1 {i}')
    run(session, 'molmap #1 2 gridSpacing 1')
    run(session, f'save vols/frame_{i}.mrc')
    #print(i, flush=True)

run(session, 'exit')
