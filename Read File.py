import sys
import binascii
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, lfilter


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y



path = '/Users/allenu/Documents/Spike Sorting/DATA Set/CA1/d5331/'

nChannels = 8
samplingRate = 10000
voltageRange = 20
voltageRangeSigned = int(voltageRange / 2)
bufferSize = 60000
nBits = 16
nBytes = nBits / 8
nBitsStep = (2 ** nBits) / 2
highCutFreq = 3000
lowCutFreq = 30
filterOrder = 5

seekLocation = 0
# data initialization
dataChannels = [[] for i in range(nChannels)]
dataChannelsFiltered = [[] for i in range(nChannels)]
couple_bytes = bytes(int(nBytes))
loopQuit = 0
test = 0
with open(path + "d533102.dat", "rb") as binary_file:
    binary_file.seek(0, os.SEEK_END)
    fileSize = binary_file.tell()
    print(fileSize)
    while loopQuit == 0:
        # check if the unextract data exist the buffer
        if (fileSize - seekLocation) <= (bufferSize * nChannels * nBytes):
            print("almost finish")
            bufferSize = int((fileSize - seekLocation) / nChannels / nBytes)
            loopQuit = 1
        # init buffer data
        dataChannelsBuffer = [[] for i in range(nChannels)]
        for i in range(0, bufferSize):
            for y in range(0, nChannels):
                binary_file.seek(seekLocation + int(i * nChannels * nBytes) + int(y * nBytes))
                couple_bytes = binary_file.read(2)
                readByteVoltage = int.from_bytes(couple_bytes, byteorder='little',
                                                 signed=True) / nBitsStep * voltageRangeSigned
                dataChannelsBuffer[y].append(readByteVoltage)
                dataChannels[y].append(readByteVoltage)

        for y in range(0, nChannels):
            dataChannelsFiltered[y].extend(butter_bandpass_filter(dataChannelsBuffer[y], lowCutFreq, highCutFreq,
                                                             samplingRate, filterOrder))
        dataChannelsBuffer.clear()
        seekLocation += int(bufferSize * nChannels * nBytes)
        #test += 1
        #print(test,seekLocation)
# print(dataChannels[3][0:1000])
t = np.arange(0, 30000, 1)
#print(dataChannelsFiltered[2][0:30000])
plt.plot(t,dataChannelsFiltered[2][0:30000])
plt.show()
