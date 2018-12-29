"""
Created on Fri Dec 28 18:07:51 2018

@author: david
"""
import numpy as np
import matplotlib.pyplot as plt
#from astropy.convolution import Gaussian2DKernel,convolve
#import scipy.linalg as linalg
#from mpl_toolkits.mplot3d import Axes3D
from scipy.io import wavfile
import sys

#name=sys.argv[1]
name="08BrainDamage.wav"

fs, data = wavfile.read(name)
chanels=np.shape(data)[1]
data=data.T
prom=np.mean(data)
stdev=np.std(data)
med=np.median(data)



fc=[]
if(chanels==1):
    fc=np.array(data)
else:
    fc=0.5*(np.array(data[0])+np.array(data[1]))
t=np.arange(len(fc))
freq=np.fft.fftfreq(t.shape[-1])
#plt.plot(freq,np.log10(abs(fc.real)+1))

FOUT=open(name.split(".wav")[0]+".txt","w")
FOUT.write("name "+str(name)+"\n")
FOUT.write("mean "+str(prom)+"\n")
FOUT.write("median "+str(med)+"\n")
FOUT.write("stddev "+str(stdev)+"\n")
FOUT.close()


    
    #freq = np.fft.fftfreq(t.shape[-1])
#FT=np.fft.fft(data)
#
#
#
#
#ret=np.fft.ifft(FT).real
#wavfile.write("BDR.wav",fs,ret)
#
