import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def histm(h2,h1):
    cdf1 = np.cumsum(h1)
    cdf2 = np.cumsum(h2)
    # print cdf2
    mapping = np.zeros_like(h1)
    for i in range(256):
        mapping[i] = np.argmin(np.abs(cdf1[i] - cdf2))
    return mapping

if __name__ == '__main__':
    im1 = mpimg.imread('/home/shubh/Documents/IP/Assignment1/lena.jpg',0)
    im2 = mpimg.imread('/home/shubh/Documents/IP/Assignment1/baboon.png',0)
    h1,_ = np.histogram(im1,bins=256)
    h2,_ = np.histogram(im2,bins=256)
    mapping = histm(h1,h2)
    out = mapping[im2]
    h3,_ = np.histogram(out,bins=256)
    fig = plt.figure()
    # print mapping
    # print h1.shape,h2.shape
    # plt.plot(np.array(range(256)),h1,'r')
    # plt.plot(np.array(range(256)),h2,'g')
    # plt.plot(np.array(range(256)),h3,'b')
    # plt.show()
    fig.add_subplot(1,3,1)
    plt.title("source")
    plt.imshow(im1)
    # fig.add_subplot(3,2,2)
    # plt.hist(im1,bins='auto')
    fig.add_subplot(1,3,2)
    plt.title("target")
    plt.imshow(im2)
    # fig.add_subplot(3,2,4)
    # plt.hist(im2,bins='auto')
    fig.add_subplot(1,3,3)
    plt.title("mapped")
    plt.imshow(out)
    # fig.add_subplot(3,2,6)
    # plt.hist(out,bins='auto')
    plt.show()