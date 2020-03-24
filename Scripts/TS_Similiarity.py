#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 11:19:52 2020

@author: matthiasboeker
Similarity matrix of all the states/ DTW """
import numpy as np 
import pandas as pd
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw


state_list = CH.sort_values(['Distance'])['Province/State'].drop_duplicates()
#Sort state_list by distance 


#Create similarity matrix / Number of states in China 
sim_matrix = np.zeros([33,33])
i = j = 0      
for state_a in state_list:
    i = 0 
    for state_b in state_list:
        vec_a = CH.loc[CH['Province/State']==state_a,'Infected'].diff().transform(lambda x: x*(100/x.max())).iloc[1:]
        vec_b = CH.loc[CH['Province/State']==state_b,'Infected'].diff().transform(lambda x: x*(100/x.max())).iloc[1:]
        sim_matrix[i,j],_ = fastdtw(vec_a,vec_b, dist=euclidean)
        i=i+1
    j=j+1
sim_matrix = pd.DataFrame(sim_matrix, index=state_list, columns=state_list)

#Create distance matrix / Number of states in China 
dist_matrix = np.zeros([33,33])
i = j = 0      
for state_a in state_list:
    i = 0 
    for state_b in state_list:
        dist_matrix[i,j] = np.square(np.power(CH.loc[CH['Province/State']==state_a,'Long'][0]-CH.loc[CH['Province/State']==state_b,'Long'][0],2)+np.power(CH.loc[CH['Province/State']==state_a,'Lat'][0]-CH.loc[CH['Province/State']==state_b,'Lat'][0],2))
        i=i+1
    j=j+1
dist_matrix = pd.DataFrame(dist_matrix, index=state_list, columns=state_list)

a = np.triu(dist_matrix)
b = np.triu(sim_matrix)
a[a==0] = np.nan
b[b==0] = np.nan

plt.scatter(a, b)
m, c = np.polyfit(a, b, 1)
plt. plot(a, m*a + c)
plt.show()

fig, ax = plt.subplots()
for state in state_list:
    plot_mat=sim_matrix.drop(state,axis=1)
    plot_mat.loc[state,:].plot()
#ax.legend(state_list)
    