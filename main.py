import sys
import numpy as np
import matplotlib.pyplot as plt
import subprogram as subprogram
path = '/Users/allenu/Documents/Spike Sorting/DATA Set/CA1/d5331/'
file_name = "d533101.dat"
frequency=10000
data = np.reshape(np.fromfile(file_name,dtype=np.int16,count=-1),(8,-1), order='F')

subprogram.plotData(data,120,121,frequency)
#subprogram.plotData(data,120,129,frequency)
plt.show()


