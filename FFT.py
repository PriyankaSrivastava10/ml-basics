#Importing the fft and inverse fft functions from fftpackage
from scipy.fftpack import fft, ifft
import numpy as np

#create an array with random n numbers
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
print (x)

#Applying the fft function
y = fft(x)
print (y)


#FFT is already in the workspace, using the same workspace to for inverse transform
yinv = ifft(y)
print (yinv)
