import matplotlib.pylab as plt
import time
from math import *

start_time = time.time()

##circle not in the middle

print 'Exercise 3.31 V2.0'


#calculate circle condition
def calculate():
    c_x.append(initial_x)
    c_y.append(initial_y)
    c_vx.append(initial_vx)
    c_vy.append(initial_vy)
    c_t.append(0)
    n=0
    for i in range(100000):
        c_x.append(c_x[i]+c_vx[i]*dt)
        c_y.append(c_y[i]+c_vy[i]*dt)
        c_vx.append(c_vx[i])
        c_vy.append(c_vy[i])
        c_t.append((i+1)*dt)
#range square
        if c_x[-1]>1.0 or c_x[-1]<-1.0:
            c_vx[-1]=-c_vx[-1]
        if c_y[-1]>1.0 or c_y[-1]<-1.0:
            c_vy[-1]=-c_vy[-1]
#range circle
        if (c_x[-1]-circle_cx)**2+(c_y[-1]-circle_cy)**2<circle_r**2 and n>5:
            v_vertical=c_vx[-1]*(c_x[-1]-circle_cx)/circle_r+c_vy[-1]*(c_y[-1]-circle_cy)/circle_r
            v_verticalx=v_vertical*(c_x[-1]-circle_cx)/circle_r
            v_verticaly=v_vertical*(c_y[-1]-circle_cy)/circle_r
            v_parallelx=c_vx[-1]-v_verticalx
            v_parallely=c_vy[-1]-v_verticaly
            v_verticalx=-v_verticalx
            v_verticaly=-v_verticaly
            c_vx[-1]=v_verticalx+v_parallelx
            c_vy[-1]=v_verticaly+v_parallely
            n=0
        n=n+1
    return 0




c_x=[]
c_y=[]
c_vx=[]
c_vy=[]
c_t=[]
#Initial conditions
dt=0.001
initial_x=0.8
initial_y=0.0
initial_vx=1.34567
initial_vy=1.0
circle_cx=0.1
circle_cy=0.1
circle_r=0.5 

circle_a=0.5
circle_b=0.5

print 'ball condition x =',initial_x,'        y =',initial_y
print '               vx =',initial_vx,'        vy =',initial_vy


#if it is a circle
if circle_a == circle_b:
    circle_r = circle_a
    
    print '                 r =',circle_r
    calculate()
    plt.figure(figsize=(20,20))
    plt.scatter(initial_x,initial_y,color='blue')
    plt.scatter(c_x,c_y,s=1,color ='red')
    plt.title('Exercise 3.31 circle x='+str(circle_cx)+'  y='+str(circle_cy)+'  r='+str(circle_r))
    plt.xlabel('x(length unit)')
    plt.ylabel('y(length unit)')
    plt.xlim(-1.2,1.2)
    plt.ylim(-1.2,1.2)
#draw a square
    plt.plot([1,-1,-1,1,1],[1,1,-1,-1,1],color='black')
#draw a circle
    circle_x=[]
    circle_y=[]
    for i in range(510):
        circle_x.append(circle_r*cos(i*pi/250.0)+circle_cx)
        circle_y.append(circle_r*sin(i*pi/250.0)+circle_cy)
    plt.plot(circle_x,circle_y,color='black')
    plt.legend()
#total time used
    print 'Total time',c_t[-1],'time unit'
    print 'Time used',time.time() - start_time,'s'
    plt.show()

#total time used
    print 'Total time',c_t[-1],'time unit'
    print 'Time used',time.time() - start_time,'s'
    plt.show()