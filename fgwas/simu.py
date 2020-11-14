'''
Author: jirufengyu
Date: 2020-11-09 05:30:42
LastEditTime: 2020-11-14 02:29:58
LastEditors: jirufengyu
Description: Nothing
FilePath: /PINNs/fgwas/simu.py
'''
from math import exp
import numpy as np
def runif(num,minx=0,maxx=1):
    #产生num个从min到max的随机float型随机数,类型为ndarray
    rand=(maxx-minx)*np.random.random(num)+minx
    return rand
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

        mc = get_mean_vector(pheT, pheY)        #[t,y]
        mc_t = mc["t"][np.where(mc["y"]>0)]
        mc_y = mc["y"][np.where(mc["y"]>0)]
        m = len(mc_t)-1
        if(m==0):
            mc = get_mean_vector(pheY, pheT)
            mc_y = mc["y"] - min(mc["y"])*1.01

        par = []
        ls_i = ls_max = float("inf")
        minx=np.delete(mc_y,[0])
        maxx=np.delete(mc_y,[m])
        a_rate = np.mean(minx/maxx)
        if(a_rate==1) :
            a_rate = 0.99
        for i in range(1,11):
            par_a = mc_y[m] * a_rate**i

            try:
                par_r=(np.log(par_a/mc_y[0]-1) - np.log(par_a/mc_y[m]-1))/(mc_t[0]-mc_t[m])
            except:
                continue;
            par_b = (par_a / mc_y[m] -1)/exp(-par_r*mc_t[m])
            #print(type((1+par_b*np.exp(-par_r*mc_t))))
            
            y_ls = np.sum(np.abs(mc_y - par_a/(1+par_b*np.exp(-par_r*mc_t)))**2)
            
            if (y_ls < ls_max):
            
                ls_i = i
                ls_max = y_ls
                par = [par_a, par_b, par_r]
            
        rand=runif(len(par),0.95,1.05)
        result=list(map(lambda x,y:x*y,par,rand))                  #两列表相乘
        #print(result)
        return result
y=np.linspace(1,20,20,dtype=np.int)
t=np.linspace(11,30,20,dtype=np.int)

c=Curve()
print(c.log_est_init_param(y,t))

def fin_generate_bc_marker( n_obs, dist ):

    if (dist[1] != 0):
        cm=c(0, dist)/100
    else:
        cm=dist/100
  
    n  = len(cm)
    rs = 1/2*( np.exp(2*cm) - np.exp(-2*cm) ) / (np.exp(2*cm)+np.exp(-2*cm))
    mk = array( 0, dim=c( n_obs, n ) )
  
    for j in 1:n_obs:
        mk[j,1] = ( runif(1)>0_5 )
  
    for i in 2:n:
        for  j in 1:n_obs :
        
            if (mk[j,i-1]==1)
                mk[j,i] = ( runif(1)>rs[i] )
            else
                mk[j,i] = ( runif(1)<rs[i] )
        
  
    return mk
