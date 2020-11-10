'''
Author: jirufengyu
Date: 2020-11-09 05:30:42
LastEditTime: 2020-11-09 16:34:47
LastEditors: jirufengyu
Description: Nothing
FilePath: /PINNs/fgwas/simu.py
'''
from math import exp
import numpy as np
def get_mean_vector(pheT,pheY):
    """
    input:
        t=np.linspace(11,30,20,dtype=np.int)
        y=np.linspace(1,20,20,dtype=np.int)
    return
        [array([11.  , 11.95, 12.9 , 13.85, 14.8 , 15.75, 16.7 , 17.65, 18.6 ,
                19.55, 21.45, 22.4 , 23.35, 24.3 , 25.25, 26.2 , 27.15, 28.1 ,
                29.05, 30.  ]), 
       [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0,
        13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]]
    """
    t_count=len(np.unique(pheT))
    if t_count>=20:
        t_min=min(pheT)
        t_max=max(pheT)
        print(t_min)
        print(t_max)
        pheT=np.round((pheT-t_min)/(t_max-t_min)*20)/20*(t_max-t_min)+t_min
    t=np.unique(pheT)
    t_all=np.sort(t)
   
    y_all=[]
    for t in t_all:
        y_all.append(np.mean(pheY[int(np.argwhere(pheT==t))]))
    y_all=np.asarray(y_all)
    return {"t":t_all,"y":y_all}
##-----------------------------------------------------------
## Logistic curve
##
##    y = a/(1+b*exp(-r*t))
##
##-----------------------------------------------------------
class Curve:
    def log_get_curve(self,par,times):
        y=par[1]/(1+par[2]*exp(-1*par[3]*times))
        return y
    def log_get_gradient(self,par,times):
        d_a=1/(1+par[2]*exp(-1 * par[3]*times) )
        d_b=(-1)*par[1]/((1+par[2]*exp(-1 * par[3]*times))^2)*exp(-1*par[3]*times)
        d_r=(-1)*par[1]/((1+par[2]*exp(-1 * par[3]*times))^2)*par[2]*exp(-1*par[3]*times)*(-1*times)
        return list(d_a,d_b,d_r)
    def log_get_simu_param(self, times, ):
        return np.asarray([[18.18,9.98,0.99],[17.08,9.78,0.97],[15.95,9.88,0.98]])

    def log_est_init_param(self, pheY,  pheT):

        mc = get_mean_vector(pheY, pheT)        #[t,y]
        mc_t = mc["t"][np.where(mc["y"]>0)]
        mc_y = mc["y"][np.where(mc["y"]>0)]
        m = len(mc_t)-1
        if(m==0):
            mc = get_mean_vector(pheY, pheT)
            mc_y = mc["y"] - min(mc["y"])*1.01

        par = []
        ls_i = ls_max = float("inf")
        a_rate = np.mean(mc_y[-1]/mc_y[-m])
        if(a_rate==1) :
            a_rate = 0.99
        for i in range(1,10):
        
            par_a = mc_y[m] * a_rate**i
            #par_r = try( (log(par.a/mc.y[1]-1) - log(par.a/mc.y[m]-1))/(mc.t[1]-mc.t[m]))
            try:
                par_r=(np.log(par_a/mc_y[1]-1) - np.log(par_a/mc_y[m]-1))/(mc_t[1]-mc_t[m])
            except:
                continue;

            par_b = (par_a / mc_y[m] -1)/exp(-par_r*mc_t[m])
            
            y_ls = sum(abs(mc_y - par_a/(1+par_b*exp(-par_r*mc_t)))**2)

            if (y_ls < ls_max):
            
                ls_i = i
                ls_max = y_ls
                par = [par_a, par_b, par_r]
            
        
        rand=0.1*np.random.random(len(par))+0.95
        result=list(map(lambda x,y:x*y,par,rand))                  #两列表相乘
        return result
t=np.linspace(11,30,20,dtype=np.int)
y=np.linspace(1,20,20,dtype=np.int)
c=Curve()
print(c.log_est_init_param(y,t))