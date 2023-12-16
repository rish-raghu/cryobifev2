# adapted from Ellen Zhong

from cryodrgn import mrc
import numpy as np
import os

D = 64
APIX=1
files = os.listdir('vols')
for t, file in enumerate(files):
    data, header = mrc.parse_mrc(f'vols/{file}')
    x,y,z = data.shape
    new = np.zeros((D, D, D), dtype=np.float32)
    i, j, k = (D-x)//2, (D-y)//2, (D-z)//2
    new[i:(i+x),j:(j+y),k:(k+z)] = data
    
    xorg,yorg,zorg = header.get_origin()
    xorg -= APIX*k
    yorg -= APIX*j
    zorg -= APIX*i

    mrc.write(f'vols_pad/{file}', new, Apix=APIX, xorg=xorg, yorg=yorg, zorg=zorg)
    print(t, flush=True)
