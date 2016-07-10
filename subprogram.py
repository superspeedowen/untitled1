import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

def plotData(data,start,end,frequency):
    fig, axs = plt.subplots(4, sharex=True, sharey=True)
    t = np.arange(start,end,1/frequency)
    plt.ticklabel_format(useOffset=False)
    for n in range(0,4):
        axs[n].plot(t,data[n+1,(start*frequency):(end*frequency)])
    fig.subplots_adjust(hspace=0)
    plt.setp([a.get_xticklabels() for a in fig.axes[:-1]], visible=False)

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, b,a):
    y = lfilter(b, a, data)
    return y