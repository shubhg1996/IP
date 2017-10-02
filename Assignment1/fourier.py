import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

if __name__ == '__main__':
    im1 = mpimg.imread('/home/shubh/Documents/IP/Assignment1/lena.jpg',0)
    ffsh = np.fft.fftshift(np.fft.fft2(im1))
    ffabs = 20*np.log10(abs(ffsh))
    ffph = np.angle(ffsh)

    iffabs = np.fft.ifftshift(np.fft.ifft(abs(ffsh)))
    iffph = np.fft.ifft2(np.exp(ffph*1j))
    fig = plt.figure()
    # print h1.shape,h2.shape
    # plt.plot(np.array(range(256)),h1,'r')
    # plt.plot(np.array(range(256)),h2,'g')
    # plt.plot(np.array(range(256)),h3,'b')
    # plt.show()
    fig.add_subplot(2,3,1)
    plt.title('Image')
    plt.imshow(im1)
    fig.add_subplot(2,3,2)
    plt.title('fourier magnitude')
    plt.imshow(ffabs)
    fig.add_subplot(2,3,3)
    plt.title('fourier phase')
    plt.imshow(ffph)
    fig.add_subplot(2,3,4)
    plt.title('recon magnitude')
    plt.imshow((iffabs).astype(np.uint8))
    fig.add_subplot(2,3,5)
    plt.title('recon phase')
    plt.imshow(abs(iffph))
    plt.show()