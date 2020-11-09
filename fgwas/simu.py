from math import exp
import numpy as np
def get_mean_vector(pheY, pheT):
	t_count = length(np.unique(pheT))
	if(t_count>=20):
		t_min = min(pheT)
		t_max = max(pheT)
		pheT = round((pheT - t_min)/(t_max-t_min)*20)/20*(t_max-t_min) + t_min
    t=np.unique(pheT)
	t_all = t.sort(reverse=False)
	y_all = []
	for t in t.all:
		y_all = list( y_all, mean(pheY[which(pheT==t)]) )

	return list(t=t_all, y=y_all)
f=[1,2,3,4,5,6]
y=[2,4,6,8,10,12]
print(get_mean_vector(y,f))
class Curve:
##-----------------------------------------------------------
## Logistic curve
##
##    y = a/(1+b*exp(-r*t))
##
##-----------------------------------------------------------
    def log_get_curve(self,par,times):
        y=par[1]/(1+par[2]*exp(-1*par[3]*times))
        return y
    def log_get_gradient(self,par,times):
        d_a=1/(1+par[2]*exp(-1 * par[3]*times) )
        d_b=(-1)*par[1]/((1+par[2]*exp(-1 * par[3]*times))^2)*exp(-1*par[3]*times)
        d_r=(-1)*par[1]/((1+par[2]*exp(-1 * par[3]*times))^2)*par[2]*exp(-1*par[3]*times)*(-1*times)
        return list(d_a,d_b,d_r)
    def log_get_simu_param(object, times, options=list()):
        return np.asarray([[18.18,9.98,0.99],[17.08,9.78,0.97],[15.95,9.88,0.98]])
    '''
    def log_est_init_param(object, pheY, pheX, pheT, options=list()):

        mc = get_mean_vector(pheY, pheT)
        mc.t = mc.t[mc.y>0]
        mc.y = mc.y[mc.y>0]
        m = length(mc.t)
        if(m==0):
            mc = get_mean_vector(pheY, pheT)
            mc.y = mc.y - min(mc.y)*1.01

        par = c()
        ls.i = ls.max = Inf
        a.rate = mean(mc.y[-1]/mc.y[-m])
        if(a.rate==1) :
            a.rate = 0.99
        for i in range(1,10):
        
            par.a = mc.y[m] * a.rate^i
            par.r = try( (log(par.a/mc.y[1]-1) - log(par.a/mc.y[m]-1))/(mc.t[1]-mc.t[m]))
            if(class(par.r)=="try-error" || is.infinite(par.r) )
                next

            par.b = (par.a / mc.y[m] -1)/exp(-par.r*mc.t[m])

            y.ls = sum(abs(mc.y - par.a/(1+par.b*exp(-par.r*mc.t)))^2, na.rm=T)

            if (y.ls < ls.max):
            
                ls.i = i
                ls.max = y.ls
                par = c(par.a, par.b, par.r)
            
        

        return (par*runif(length(par),0.95, 1.05) )'''
