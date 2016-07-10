import sys
import numpy as np
import matplotlib.pyplot as plt
import subprogram as subprogram
path = '/Users/allenu/Documents/Spike Sorting/DATA Set/CA1/d5331/'
file_name = "d533101.dat"
sample_frequency=10000
data = np.reshape(np.fromfile(file_name,dtype=np.int16,count=-1),(8,-1), order='F')

# subprogram.plotData(data,120,128,sample_frequency)
# #subprogram.plotData(data,120,129,sample_frequency)
# plt.show()

datasample = data[0:4,0:60*sample_frequency]



