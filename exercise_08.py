import pylab as pl
import math
class bifurcation_diagram:
    def __init__(self,q=0.5,g=9.8,l=9.8,O_D=2.0/3.0,Fd=1.35,theta=0.20):
        self.omega=[0]
        self.theta=[theta]
        self.q=q
        self.g=g
        self.l=l
        self.O_D=O_D
        self.Fd=Fd
        self.t=[0]
        self.dt=2*math.pi/(500*O_D)
        self.T=[]
        self.Theta=[]
        self.Omega=[]
        self.fd=[]
    def calculate(self):
        for i in range(7500):
            self.t.append(self.t[i] + self.dt)
            
            temp_omega=self.omega[-1]-(self.g/self.l)*\
            math.sin(self.theta[-1])*self.dt -self.q*self.omega[-1]*self.dt +\
            self.Fd*math.sin(self.O_D*self.t[-1])*self.dt
            self.omega.append(temp_omega)            
            temp_theta=self.theta[-1]+self.omega[-1]*self.dt    
            if(temp_theta>=math.pi):
                 temp_theta-=2*math.pi
            if(temp_theta<=-math.pi):
                 temp_theta+=2*math.pi
            self.theta.append(temp_theta)
            
        for i in range(10):
            self.Theta.append(self.theta[500*(i+5)])
            self.Omega.append(self.omega[500*(i+5)])
            self.fd.append(self.Fd)
            
            
                
    def show_results(self):
        pl.plot(self.fd, self.Theta,'g.')
        pl.title('$Bifurcatioin$ $diagram$')
        pl.xlabel('$F_{D}$')
        pl.ylabel('$\\theta$(radians)')
        pl.show()
        

for i in range(150):
    a=bifurcation_diagram(Fd=1.35+i/1000.0)
    a.calculate()
    a.show_results()