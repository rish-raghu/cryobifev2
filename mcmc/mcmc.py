import argparse
import os
import numpy as np
from numba import jit 
import matplotlib.pyplot as plt


@jit(nopython=True)
def compute_pGImgs(Gs, logprobs):
    # note: all probabilities are in log scale
    N = logprobs.shape[0] # number of images
    pVolG = np.exp(-Gs) # compute p(volume | G)
    pVolG = np.log(pVolG / np.sum(pVolG))
    pGImgs = -np.log(np.sum(np.diff(Gs)**2)) # compute prior p(G)
    for n in range(N):
        # compute P(image | volumes) using log-sum-exp trick
        pImgVols = logprobs[n, :] + pVolG
        pImgVolsMax = np.max(pImgVols)
        pGImgs += (pImgVolsMax + np.log(np.sum(np.exp(pImgVols - pImgVolsMax))))
    return pGImgs


@jit(nopython=True)
def mcmc(T, logprobs):
    M = logprobs.shape[1] # number of volumes
    allGs = np.zeros((T+1, M))
    allpGImgs = np.zeros(T+1)
    
    # initialize G
    Gs = 4 * np.random.rand(M) - 2
    Gs -= (np.sum(Gs)/M)
    pGImgs = compute_pGImgs(Gs, logprobs)
    allGs[0, :] = Gs
    allpGImgs[0] = pGImgs

    for t in range(T):
        GsPrev = Gs.copy()
        pGImgsPrev = pGImgs

        node = np.random.randint(0, M) # randomly select node
        deltaG = np.random.rand() - 0.5 
        Gs[node] += deltaG # randomly displace FE at node
        Gs -= (np.sum(Gs)/M) # shift G s.t. sum is 0

        pGImgs = compute_pGImgs(Gs, logprobs)
        acceptProb = pGImgs - allpGImgs[t]
        
        # if move rejected, reset G
        if (np.log(np.random.rand()) > acceptProb):
            Gs = GsPrev
            pGImgs = pGImgsPrev

        allpGImgs[t+1] = pGImgs
        allGs[t+1, :] = Gs
    
    return allGs, allpGImgs


if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Run monte carlo to estimate FES")
    parser.add_argument('logprobs', help='.npy file with log probabilities')
    parser.add_argument('T', type=int, help='number of MC steps')
    parser.add_argument('-o', required=True, help='output directory')
    args = parser.parse_args()

    logprobs = np.load(args.logprobs).T
    allGs, allpGImgs = mcmc(args.T, logprobs)
    np.save(os.path.join(args.o, 'mcfes.npy'), allGs)
    np.save(os.path.join(args.o, 'mcfesprob.npy'), allpGImgs)


    # logratios = logprobs - logprobs[:, 0, np.newaxis]
    # ratios = np.exp(logratios)
    # probs = ratios / np.sum(ratios, axis=1)[:, np.newaxis]
    # models = np.argmax(probs, axis=1)
    # plt.plot(np.arange(20), np.mean(logprobs, axis=0))
    # plt.savefig("bioem/ctf_all_med_v2/modelHistogram.png")
    # assert False



    




