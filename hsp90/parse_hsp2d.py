import numpy as np
np.seterr(divide='ignore', invalid='ignore')
import matplotlib.pyplot as plt
import seaborn as sns

logprobs = np.loadtxt("bioem/all_images.txt")
logratios = logprobs - logprobs[:, 0, np.newaxis]
ratios = np.exp(logratios)
probs = ratios / np.sum(ratios, axis=1)[:, np.newaxis]

modelByImg = np.argmax(probs, axis=1)
modelCounts = np.bincount(modelByImg).reshape((15, 15))

sns.heatmap(modelCounts)
plt.savefig("bioem/2dFES.png")
