import numpy as np
import matplotlib.pyplot as plt

def lmaxq(inp):
    levels = 4
    m = np.linspace(inp.min()-np.finfo(float).eps,inp.max()+np.finfo(float).eps,levels+1)
    out = np.zeros_like(inp)
    mse = np.zeros((100,1))
    cent = np.zeros((levels,1))
    for iter in range(100):
        for level in range(levels):
            mask1 = inp<m[level+1]
            mask2 = inp>=m[level]
            mask = np.bitwise_and(mask1,mask2)
            roi = inp[mask]
            cent[level] = np.mean(roi)
        for level in range(1,levels):
            m[level] = (cent[level]+cent[level-1])/2
        for t in range(len(inp)):
            for level in range(levels):
                if inp[t]<m[level+1]:
                    out[t] = cent[level]
                    break
        mse[iter] = ((out - inp) ** 2).mean(axis=None)
    plt.plot(np.array(range(100)),mse)
    # plt.plot(np.array(range(100)),inp,'r')
    # plt.plot(np.array(range(100)),out,'g')
    print "Transition levels"
    print m
    print "Representation levels"
    print cent
    plt.show()

if __name__=="__main__":
    inp = np.random.normal(0,1,100)
    lmaxq(inp)