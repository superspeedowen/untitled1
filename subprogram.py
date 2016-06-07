import numpy as np
import matplotlib.pyplot as plt

def plotData(data,start,end,frequency):
    fig, axs = plt.subplots(4, sharex=True, sharey=True)
    t = np.arange(start,end,1/frequency)
    for n in range(0,4):
        axs[n].plot(t,data[n+1,(start*frequency):(end*frequency)])
    fig.subplots_adjust(hspace=0)
    plt.setp([a.get_xticklabels() for a in fig.axes[:-1]], visible=False)
