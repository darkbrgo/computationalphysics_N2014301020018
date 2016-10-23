import pylab as pl
import math
initial_theta=math.pi/8
initial_v=565
class cannon:
    def __init__(self,x=0,y=0,time_step=0.1,g=6.67*10**-11,
                 rearth=6371000,mearth=5.977*10**24,totle_time=60,
                 B=0.000045,m=1,cr_x=24000,cr_y=-2100,a=0.0065,
                 alpha=2.5,b2=0.00004,T0=288,
                 initial_vx=initial_v*math.cos(initial_theta),
                 initial_vy=initial_v*math.sin(initial_theta)):
        self.vx=[initial_vx]
        self.vy=[initial_vy]
        self.dt=time_step
        self.G=g
        self.R=rearth
        self.M=mearth
        self.m=m
        self.B2=[b2/m]
        self.x=[x]
        self.y=[y]
        self.t=[0]
        self.a=a
        self.alpha=alpha
        self.T0=T0
        self.time=totle_time
        self.x0=cr_x
        self.y0=cr_y
    def trajectory(self):
        _time = 0
        while(_time < self.time):
            self.B2.append(self.B2[-1]*(1-self.a*self.y[-1]/self.T0)**self.alpha)
            self.x.append(self.x[-1]+\
                          self.vx[-1]* self.dt)
            self.vx.append(self.vx[-1]-self.B2[-1]*math.sqrt((self.vx[-1])**2+\
                           (self.vy[-1])**2)*self.vx[-1]/self.m*self.dt)
            self.vy.append(self.vy[-1] -\
                          self.dt * self.G * self.M / (self.R + self.y[-1])**2-\
                          self.B2[-1]*math.sqrt((self.vx[-1])**2+(self.vy[-1])**2)*\
                          self.vy[-1]/self.m*self.dt)
            self.y.append(self.y[-1] +\
                          self.vy[-1] * self.dt)
            self.t.append(_time)
            _time += self.dt    
    def show_results(self):
        font = {'family': 'serif',
                'color':  'darkblue',
                'weight': 'normal',
                'size': 16,
        }
        pl.plot(self.x, self.y)
        pl.plot(self.x0,self.y0,"r*")
        pl.title('Trajectory of cannon shell', fontdict = font)
        pl.xlim(0,28000)
        pl.ylim(-3000,3000)
        pl.xlabel('x ($m$)')
        pl.ylabel('y ($m$)')
        pl.show()

a= cannon()
a.trajectory()
a.show_results()
