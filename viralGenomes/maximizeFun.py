import numpy as np
from scipy.optimize import minimize
from matplotlib import pyplot as plt

def fun(x):
    return -(x[0]*x[1]/(x[2]+x[7])*np.exp(-x[3]*x[7])*x[3]*x[7] + x[1]/(x[2]+x[7])*(1-x[4]**(x[5]*x[7]*(x[6]*x[7]/3-x[5]*x[7])/(x[6]*x[7]/3-1)))*x[5]*x[7]*(1-x[0]*x[1]/(x[2]+x[7])*np.exp(-x[3]*x[7])*x[3]*x[7]))


def main():
    x0 = np.array([1, 40, 3000, 10**(-5), .79, 10**(-5), .12, 10000])

    #res = minimize(fun, x0, method='SLSQP', bounds=((0,10),(0,80),(0,100000),(10**(-8),10**(-4)),(0,1),(10**(-8),10**(-4)),(0,1),(0,500000)), options={'disp': True, 'ftol':1e-40})

    #print(res.x)

    l = np.linspace(0,50000,50001)

    rate_nuc = (x0[3]+x0[6]*x0[5])*(np.exp(-x0[3]*l/3)+x0[4]**(9*x0[5]*l**2*(x0[6]-x0[5])/(4*x0[6]*l-16))-1)
    rate_genome = l*(x0[3]+x0[6]*x0[5])*(np.exp(-x0[3]*l/3)+x0[4]**(9*x0[5]*l**2*(x0[6]-x0[5])/(4*x0[6]*l-16))-1)
    rate_time = (x0[1]*l/(x0[2]+l))*(x0[3]+x0[6]*x0[5])*(np.exp(-x0[3]*l/3)+x0[4]**(9*x0[5]*l**2*(x0[6]-x0[5])/(4*x0[6]*l-16))-1)
    rate_time2 = (x0[1] * l / (x0[2] + l)) * (10**-7 + x0[6]*x0[5]) * (
                np.exp(-10**-7 * l / 3) + x0[4] ** (9 * x0[5] * l ** 2 * (x0[6] - x0[5]) / (4 * x0[6] * l - 16)) - 1)
    plt.figure(figsize=(16, 9))

    # Remove the plot frame lines. They are unnecessary chartjunk.
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)
    #ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Ensure that the axis ticks only show up on the bottom and left of the plot.
    # Ticks on the right and top of the plot are generally unnecessary chartjunk.
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    # Make sure your axis ticks are large enough to be easily read.
    # You don't want your viewers squinting to read your plot.
    plt.xticks([0,50000],[0,50000],fontsize=36)
    plt.yticks([0,0.0003],['0','3e-4'],fontsize=36)
    m_max=rate_time.argmax()
    n_max = rate_time2.argmax()

    print(m_max,n_max)




    fig = plt.plot(l, rate_time, linewidth=5, color='olive', label='mu = 1e-5')
    fig = plt.plot(l, rate_time2, linewidth=5, linestyle='--', color='olive', label='mu = 1e-7')
    fig = plt.legend(fontsize=24)
    plt.savefig('rate_time2.png', bbox_inches="tight")
    plt.show()
main()