#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:45:29 2020
@author: matthiasboeker
Support Functions"""

#Prints out each region listed 
def get_region_list():
    print(data[0]['Province/State'].drop_duplicates().values)

#Prints out the data for the search Region/Country and the wanted dataset
#Infected: 0
#Deaths: 1
#Recovered: 2
def country_filter(dat, Country='Germany' ,Region='Germany'):
    out = dat.loc[dat['Province/State']==Region,:]
    out = dat.loc[dat['Country/Region']==Country,:]
    out.index = out['Date']
    out = out.sort_index(ascending=True)
    return out 

    
def cut_down(data):
    #Processing of the data 
    dat = data[0]
    #Delete last row 
    dat = dat.iloc[:-1,:]
    
    #Specifiy only Country/ Regions
    dat.loc[dat['Province/State']=='','Province/State'] = dat.loc[dat['Province/State']=='','Country/Region']
    dat['Long'] = dat['Long'].astype(str)
    dat['Long'] = dat['Long'].astype(float)
    dat['Lat'] = dat['Lat'].astype(str)
    dat['Lat'] = dat['Lat'].astype(float)
    dat['Date'] = dat['Date'].astype(str)
    dat['Date'] = dat['Date'].astype('datetime64[ns]')
    dat['Infected'] = dat['Infected'].astype(str)
    dat['Infected'] = dat['Infected'].astype(int)
    dat['Deaths'] = data[1].iloc[:,-1].astype(str)
    dat['Deaths'] = dat['Deaths'].astype(int)
    dat['Recovered'] = data[2].iloc[:,-1].astype(str) 
    dat['Recovered'] = dat['Recovered'].astype(int) 
          
    return dat

def cosine_sim(vec_a,vec_b):
    
    
    cp = sum(vec_a[:].T*vec_b[:].T)
    sum_a = np.sum(vec_a**2)
    sum_b = np.sum(vec_b**2)
    
    cos_sim = cp/(np.square(sum_a)*np.square(sum_b))
    
    if cos_sim.shape != (1,):
        print('Wrong Dimensions of input vectors, please transform with .T')
    else:
        
        return cos_sim