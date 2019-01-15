import numpy as np
import matplotlib.pyplot as plt


def shooting(x, y):
    result = 0
    if np.sqrt(x**2 + y**2) <=1:
        result = 1
    return result


r = 3  # number of runs
N = 1000  # number of tries


for j in range(r):

    h = 0  # initial number of hits
    pi = np.array([0])  # array with initial value for pi

    # creating empty arrays for x and y for hit and miss
    xs_h = np.array([])
    ys_h = np.array([])
    xs_m = np.array([])
    ys_m = np.array([])

    for i in range(1, N+1):
        print('run %d of %d with frame %d of %d' % (j+1, r, i, N))

        x, y = np.random.random(2)
        h += shooting(x, y)

        if shooting(x, y) is 1:
            xs_h = np.append(xs_h, x)
            ys_h = np.append(ys_h, y)
        else:
            xs_m = np.append(xs_m, x)
            ys_m = np.append(ys_m, y)

        pi = np.append(pi, 4*h/i)

        plt.figure(figsize=(7, 3))
        plt.suptitle('$\pi=$' '%f' % pi[-1])

        plt.subplot(121)
        plt.plot(pi)
        plt.axhline(y=np.pi, color='r', linestyle=':', alpha=0.5)
        plt.xlim(0, i)
        plt.ylim(0, 5)

        plt.subplot(122, aspect='equal')
        plt.plot(xs_h, ys_h, 'ro', alpha=0.5, markersize=4)
        plt.plot(xs_m, ys_m, 'ko', alpha=0.5, markersize=4)
        plt.plot(x, y, 'ko', markersize=5)
        plt.plot(0, 'ro', markersize=332, alpha=0.2)
        plt.xlim(0, 1)
        plt.ylim(0, 1)

        #plt.show()
        plt.savefig('./plots/run%02d_frame%04d.jpg' % (j+1, i), bbox_inches='tight')
        plt.close()




