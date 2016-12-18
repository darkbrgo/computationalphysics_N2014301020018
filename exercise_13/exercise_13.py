import numpy as np
import matplotlib.pyplot
from pylab import *
from math import *
import mpl_toolkits.mplot3d
def power_spe(xe,xo):
    dx=0.01
    c=300.0 
    dt=dx/c
    length=int(1.0/dx)
    time=3000
    k=1000
    y=[[0 for i in range(length)]for n in range(time)]

    for i in range(length):
        y[0][i]=exp(-k*(i*dx-xe)**2)
        y[1][i]=exp(-k*(i*dx-xe)**2)

    r=c*dt/dx
    
    for n in range(time-2):
        for i in range(1,length-1):
            y[n+2][i]=2*(1-r**2)*y[n+1][i]-y[n][i]+r**2*(y[n+1][i+1]+y[n+1][i-1])
    y=array(y)

    yo=[]
    t=array(range(time))*dt
    for n in range(time):
        yo.append(y[n][int(xo/dx)])
    p=abs(np.fft.rfft(yo))**2
    f = np.linspace(0, int(1/dt/2), len(p))
    plot(f, p)
    xlim(0,3000)
    xlabel('Frequency(Hz)')
    ylabel('Power')
    title('Power spectrum')
    text(2000,20000,'$x_{percent}=$'+str(xo))


figure(figsize=[16,16])
subplot(221)
power_spe(0.3,0.1)
subplot(222)
power_spe(0.3,0.4)
subplot(223)
power_spe(0.3,0.5)

savefig('problem6.13.png')
show()
    
    