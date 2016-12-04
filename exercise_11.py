import pylab as pl
import math
import numpy as np

class Hyperion():
    def __init__(self,x0=1,y0=0,vx0=0,vy0=2*math.pi,theta=0,omega=0):
        self.x=[x0]     
        self.y=[y0]
        self.vx=[vx0]
        self.vy=[vy0]
        self.dt=0.0001
        self.t=[0]
        self.steps=120000
        self.theta=[theta]
        self.omega=[omega]
        self.r=[]

    def calculate(self):

        for i in range(self.steps):
            if self.theta[i]>math.pi:    
                self.theta[i]=self.theta[i]-2*math.pi
            if self.theta[i]<-math.pi:
                self.theta[i]=self.theta[i]+2*math.pi
            else:
                self.theta[i]=self.theta[i]

            self.r.append(math.sqrt(self.x[i]**2+self.y[i]**2))
            temp_vx=self.vx[i]-4*math.pi**2*self.x[i]*self.r[i]**(-3)*self.dt
            self.vx.append(temp_vx)
            temp_x=self.x[i]+self.vx[i+1]*self.dt
            temp_vy=self.vy[i]-4*math.pi**2*self.y[i]*self.r[i]**(-3)*self.dt
            self.vy.append(temp_vy)
            temp_y=self.y[i]+self.vy[i+1]*self.dt
            self.x.append(temp_x)
            self.y.append(temp_y)

            temp_omega=(self.omega[i]-self.dt*12*math.pi**2*self.r[i]**(-5)*(self.x[i]*math.sin(self.theta[i])-self.y[i]*math.cos(self.theta[i]))*(self.x[i]*math.cos(self.theta[i])+self.y[i]*math.sin(self.theta[i])))
            self.omega.append(temp_omega)
            self.theta.append(self.theta[i]+self.omega[i+1]*self.dt)
            
            self.t.append(self.t[i]+self.dt)

        
        return[self.x,self.y,self.t,self.theta,self.omega]     



v1=Hyperion(1,0,0,2*math.pi,0,0) 
HY1=v1.calculate()
v2=Hyperion(1,0,0,2*math.pi,0.01,0) 
HY2=v2.calculate()
theta1=HY1[3]
theta2=HY2[3]
t=HY1[2]
dtheta=np.array(HY2[3])-np.array(HY1[3])

pl.semilogy(t,dtheta,"b")
pl.xlabel('time(yr)')
pl.ylabel('dtheta(radians)')
pl.xlim(0,10)
pl.title('Hyperion dtheta versus time,circular orbit')
pl.show()