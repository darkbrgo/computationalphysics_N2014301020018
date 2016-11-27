import pylab as pl
import math

class KeplersLaw:
    def __init__(self,MS=2.0*10**30,GMS=4*math.pi**2,\
                 beta=2.0,\
                 M=4.9*10**24,a=0.72,e=0.007):          
        
        self.MS=MS        
        self.GMS=GMS
        self.M=M
        self.a=a
        self.e=e
        self.x=[a*(1+e)]
        self.y=[0]
        self.r=[a*(1+e)]
        self.vx=[0]
        self.vy=[(GMS*(1-e)*(1+M/MS)/(a*(1+e)))**0.5]
        self.beta=beta
        self.F=[GMS*M/(a**beta)]
        self.dt=0.002
        self.t=[0]
        self.v=[(GMS*(1-e)*(1+M/MS)/(a*(1+e)))**0.5]
        self.xshow=[a*(1+e)+e*a]
        
    def run(self):
        while(1):
            self.r.append((self.x[-1]**2+self.y[-1]**2)**0.5)
            self.F.append(self.GMS*self.M/(self.r[-1]**self.beta))
            self.vx.append(self.vx[-1]-(self.F[-1]/self.M)*self.x[-1]/self.r[-1]*self.dt)
            self.vy.append(self.vy[-1]-(self.F[-1]/self.M)*self.y[-1]/self.r[-1]*self.dt)
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
            self.v.append((self.vx[-1]**2+self.vy[-1]**2)**0.5)
            self.xshow.append(self.x[-1]+self.e*self.a)
            if(self.y[-2]<0 and self.y[-1]>=0):
                break
                   
    def showresult(self):
        
        pl.plot(self.xshow,self.y,'m-')
        pl.text(self.x[30],self.y[30],'Venus',color='red',size=20)
        pl.plot(self.e*self.a,0,'mx')

        
        pl.xlim(-0.2-max(self.xshow),0.2+max(self.xshow))
        pl.ylim(-0.2-max(self.xshow),0.2+max(self.xshow))
        pl.xlabel("X(AU)")
        pl.ylabel("Y(AU)")
        pl.show()
        
        print "a=",self.a,"e=",self.e
        print "周期T=",self.t[-1]
        print "T^2/a^3=",(self.t[-2])**2/self.a**3
        
a=KeplersLaw()
a.run()
a.showresult()