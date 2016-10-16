import pylab as pl
import math
class cannon:
    def __init__(self,coordinate_x=0,coordinate_y=0, time_step=0.1,\
                 initial_theta= math.pi/3,\
                 initial_v=70,ar_g=10,total_time=15):
        self.theta = initial_theta
        self.v = initial_v
        self.vx = [self.v * math.cos(self.theta)]
        self.vy = [self.v * math.sin(self.theta)]
        self.t = [0]
        self.x = [coordinate_x]
        self.y = [coordinate_y]
        self.g = ar_g
        self.dt = time_step
        self.time = total_time
    def calculate(self):
        _time = 0
        while(_time < self.time):
            self.x.append(self.x[-1] +\
                          self.dt * self.vx[-1])
            self.y.append(self.y[-1] +\
                          self.dt * self.vy[-1])   
            
            self.vy.append(self.vy[-1]-self.dt * self.g) 
            self.t.append(_time)
            _time += self.dt   
            
    def show_results(self):
        font = {'family': 'serif',
                'color':  'darkred',
                'weight': 'normal',
                'size': 16,
        }
        pl.plot(self.x, self.y)
        pl.title('cannon shell trajectories', fontdict = font)
        pl.xlabel('x ($m$)')
        pl.ylabel('y ($m$)')    
        pl.show()
        pl.ylim(0,200)
        pl.xlim(0,500)
a = cannon()
a.calculate()
a.show_results()