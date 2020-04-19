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
def country_filter(dat, Country='Germany' ,Region = ''):
    
    if Region == '':
        out = dat.loc[dat['Country/Region']==Country,:]
        out.index = out['Date']
        out = out.sort_index(ascending=True)
    else:
        out = dat.loc[dat['Country/Region']==Country,:]
        out = out.loc[dat['Province/State']==Region,:]
        out.index = out['Date']
        out = out.sort_index(ascending=True)       
        
    return out 

def cut_down(data):
    import numpy as np
    #Processing of the data 
    dat = data[0]
    #Delete last row 
    dat = dat.iloc[:-1,:]
    
    #Specifiy only Country/ Regions
    dat.loc[dat.loc[:,'Province/State']=='','Province/State'] = dat.loc[dat.loc[:,'Province/State']=='','Country/Region']
    dat.loc[:,'Long'] = dat.loc[:,'Long'].astype(str)
    dat.loc[:,'Lat'] = dat.loc[:,'Lat'].astype(str)
    dat.loc[:,'Date'] = dat.loc[:,'Date'].astype(str)
    dat.loc[:,'Date'] = dat.loc[:,'Date'].astype('datetime64[ns]')
    dat.loc[:,'Infected'] = dat.loc[:,'Infected'].astype(str)
    dat.loc[:,'Deaths'] = data[1].iloc[:,-1].astype(str)
    dat.loc[:,'Long'] = dat.loc[:,'Long'].astype(float)
    dat.loc[:,'Lat'] = dat.loc[:,'Lat'].astype(float)
    data[0].loc[(data[0].loc[:,'Infected']==''),'Infected'] = np.nan
    data[1].loc[(data[1].loc[:,'Deaths']==''),'Deaths'] = np.nan
    dat.loc[:,'Infected'] = dat.loc[:,'Infected'].astype(float)
    dat.loc[:,'Deaths'] = dat.loc[:,'Deaths'].astype(float)
    return dat  

def find_timepoint_zero(df):
    df["Timepoint"] = -1

    point_zero = df.loc[df['Infected']>0, "Date"][0]
    df.loc[df['Date'] == point_zero, "Timepoint"] = 0

    previous = -1
    for i, row in df.iterrows():
        if i == point_zero or previous != -1:
            previous = previous + 1
            df.at[i,'Timepoint'] = previous
            
    return df

def cosine_sim(vec_a,vec_b):
    
    
    cp = sum(vec_a[:].T*vec_b[:].T)
    sum_a = np.sum(vec_a**2)
    sum_b = np.sum(vec_b**2)
    
    cos_sim = cp/(np.square(sum_a)*np.square(sum_b))
    
    if cos_sim.shape != (1,):
        print('Wrong Dimensions of input vectors, please transform with .T')
    else:
        
        return cos_sim

