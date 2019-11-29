#In this topic we will be analyzing the FFT algorithm
#Before we begin, it is important to have some knowledge of what the fourier transform is. The fourier transform was discovered by Joseph Fourier. It allows us to analyze any given function as a sum of periodic components.
#This transform is very helpful when used as a hash function in cryptography, and it is also very useful when analysing sound digitally in the frequency spectrum on a computer.
#The FFT algorithm is defined as: sum(n-0 to N-1)e^-2PIj(kn/N)x[n]
#The inverse FFT algorithm is defined as: (1/N)sum(k=0 to N-1)e^-2PIj(kn/N)y[k]

#Here is the python implementation of the transform:
from scipy.fftpack import fft, ifft #import the scipy package
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5]) #create a sample dataset which we wish to transform
fft_x = fft(x) #here we have computed the transform of the array x
print(fft_x)
invfft_x = ifft(x) #here we have computed the inverse transform of the array x, this will return the original value.
print(invfft_x)
