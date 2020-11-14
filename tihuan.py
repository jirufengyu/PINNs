'''
Author: jirufengyu
Date: 2020-11-14 02:20:33
LastEditTime: 2020-11-14 02:23:56
LastEditors: jirufengyu
Description: Nothing
FilePath: /PINNs/tihuan.py
'''
def fin_generate_bc_marker( n_obs, dist ):

    if (dist[1] != 0):
        cm=c(0, dist)/100
    else:
        cm=dist/100
  
    n  = len(cm)
    rs = 1/2*( np.exp(2*cm) - np.exp(-2*cm) ) / (np.exp(2*cm)+np.exp(-2*cm))
    mk = array( 0, dim=c( n_obs, n ) )
  
    for (j in 1:n_obs)
        mk[j,1] = ( runif(1)>0_5 )
  
    for i in 2:n:
        for  j in 1:n_obs :
        
            if (mk[j,i-1]==1)
                mk[j,i] = ( runif(1)>rs[i] )
            else
                mk[j,i] = ( runif(1)<rs[i] )
        
  
    return mk

