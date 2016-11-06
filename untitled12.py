import pylab as pl
import math
class pendulums:
    def __init__(self,q=0.5,g=9.8,l=9.8,O_D=2.0/3.0,time_step=0.04,FD=1.2,\
    totaltime=100,theta1=0.20,theta2=0.201):
        self.omega1=[0]
        self.omega2=[0]
        self.theta1=[theta1]
        self.theta2=[theta2]
        self.q=q
        self.g=g
        self.l=l
        self.O_D=O_D
        self.FD=FD
        self.cth=[theta2-theta1]
        self.t=[0]
        self.dt=time_step
        self.time=totaltime
        self.nsteps = int(totaltime // time_step + 1)
        self.k=[math.log(self.cth[0])]
    def calculate(self):
        for i in range(self.nsteps):
            self.t.append(self.t[i] + self.dt)
            
            temp_omega1=self.omega1[-1]-(self.g/self.l)*\
            math.sin(self.theta1[-1])*self.dt -self.q*self.omega1[-1]*self.dt +\
            self.FD*math.sin(self.O_D*self.t[-1])*self.dt
            self.omega1.append(temp_omega1)            
            temp_theta1=self.theta1[-1]+self.omega1[-1]*self.dt
            if(temp_theta1>=math.pi):
                 temp_theta1-=2*math.pi
            if(temp_theta1<=-math.pi):
                 temp_theta1+=2*math.pi
            self.theta1.append(temp_theta1)
            
            temp_omega2=self.omega2[-1]-(self.g/self.l)*\
            math.sin(self.theta2[-1])*self.dt -self.q*self.omega2[-1]*self.dt +\
            self.FD*math.sin(self.O_D*self.t[-1])*self.dt
            self.omega2.append(temp_omega2)            
            temp_theta2=self.theta2[-1]+self.omega2[-1]*self.dt
            if(temp_theta2>=math.pi):
                 temp_theta2-=2*math.pi
            if(temp_theta2<=-math.pi):
                 temp_theta2+=2*math.pi
            self.theta2.append(temp_theta2)
            D=abs(self.theta2[-1]-self.theta1[-1])
            self.cth.append(math.log(D))
            self.k.append(math.log(self.cth[0])+0.0810*self.t[i])
    def show_results(self):
        pl.plot(self.t, self.cth)
        pl.plot(self.t, self.k,'--')
        pl.show()
       
a=pendulums()
a.calculate()
a.show_results()
