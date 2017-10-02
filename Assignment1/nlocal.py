import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import skimage.util as sut
from skimage import color

def nlm(img):
    H,W = img.shape
    fsize = 50
    h = 1
    h2 = h**2
    out = np.zeros_like(img)
    for x,y in np.ndindex((W,H)):
        print x,y
        wtsum = 0
        tmp = 0
        for i,j in np.ndindex((W,H)):
            wt = np.exp(-((i-x)**2+(j-y)**2)/h2)
            tmp = tmp + wt*img[j,i]
            wtsum = wtsum + wt
        out[y,x] = tmp/wtsum
    return out
if __name__ == '__main__':
    im1 = mpimg.imread('/home/shubh/Documents/IP/Assignment1/100.jpg',0)
    im1 = color.rgb2gray(im1)
    gnim = sut.random_noise(im1,mode='gaussian')
    unim = sut.random_noise(im1,mode='s&p')
    outg = nlm(gnim)
    print "outg done"
    outu = nlm(unim)
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
    plt.title('Gaussian N')
    plt.imshow(gnim)
    fig.add_subplot(2,3,3)
    plt.title('Impulse N')
    plt.imshow(unim)
    fig.add_subplot(2,3,4)
    plt.title('Denoise Gauss')
    plt.imshow(outg)
    fig.add_subplot(2,3,5)
    plt.title('Denoise Impulse')
    plt.imshow(outu)
    plt.show()