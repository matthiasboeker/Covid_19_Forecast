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
def country_filter(Region='Germany'):
    out = dat.loc[dat['Province/State']==Region,:]
    return out 

    
def cut_down(data):
    #Processing of the data 
    dat = data[0]
    #Delete the Geoposition
    dat = dat.drop(['Lat','Long'], axis=1)
        
    #Specifiy only Country/ Regions
    dat.loc[dat['Province/State']=='','Province/State'] = dat.loc[dat['Province/State']=='','Country/Region']
    dat = dat.drop('Country/Region', axis= 1)
    dat['Deaths'] = data[1].iloc[:,-1]
    dat['Recovered'] = data[2].iloc[:,-1]        
    return dat
