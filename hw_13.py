import numpy as np
import matplotlib.pyplot as plt
import sys


def CentralLimit(N):
    array = []
    for i in range (0, N):
        a = np.random.beta(0.5, 0.6, size=100)
        array.append(sum(a)/len(a))
    return array



n = int(sys.argv[1])
plt.rc('font', size=5)    




fig, axs = plt.subplots(2, 2)
arr0 = np.random.beta(0.5, 0.6, size=10000)
axs[0,0].hist(arr0, bins=500, range = (-4.,16.), density=True)
axs[0,0].set_title('Beta distribution')

axs[0,1].hist(CentralLimit(int(0.25*n)),bins=int(1.+10.*np.log(0.25*n)),density=True)
axs[0,1].set_title('Distribution of the means with N =' + str(int(0.25*n)) + ' samples')

axs[1,0].hist(CentralLimit(int(0.5*n)),bins=int(1.+10.*np.log(0.5*n)),density=True)
axs[1,0].set_title('Distribution of the means with N =' + str(int(0.5*n)) + ' samples')

axs[1,1].hist(CentralLimit(n),bins=int(1.+10.*np.log(n)),density=True)
axs[1,1].set_title('Distribution of the means with N =' + str(int(n)) + ' samples')
plt.show()
