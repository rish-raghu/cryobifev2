import numpy as np 
import MDAnalysis as mda
from MDAnalysis.analysis import rms

u = mda.Universe('../mdsim/peptide_box.gro', '../mdsim/prod_align.xtc')
T = len(u.trajectory)
Nterm = u.atoms[0]
Cterm = u.atoms[70]

dists = np.zeros(T)
for t, fr in enumerate(u.trajectory):
    dists[t] = np.sum((Nterm.position - Cterm.position)**2)**0.5

M = 10
nodes = np.zeros(M, dtype=int)
node_dists = np.linspace(dists.min(), dists.max(), M)
for i in range(M):
    nodes[i] = np.abs(dists - node_dists[i]).argmin()
np.save('node_idxs.npy', nodes)

rmsds = np.zeros((T, M))
for i, node in enumerate(nodes):
    R = rms.RMSD(u, u, select='backbone', ref_frame=node)
    R.run()
    rmsds[:, i] = R.rmsd[:, 2]

lam = 50
exps = np.exp(-lam * rmsds**2)
numer = np.sum(np.arange(M)[np.newaxis, :] * exps, axis=1)
denom = np.sum(exps, axis=1)
cvs = numer / denom / (M-1)
np.save('path_cvs.npy', cvs)
