#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 22:53:23 2020

@author: matthiasboeker
"""
import pandas as pd
import os 

os.chdir('/Users/matthiasboeker/Desktop/Covid_19_Forecast/Data')
data_files = []
for file in os.listdir():
    if file.endswith('.csv'):
        data_files.append(file)
        #data_list = data_list
    
features=[]
for i in range(0,len(data_files)):        
    data =pd.read_csv(data_files[i], sep=',', skiprows=3, encoding= 'unicode_escape')
    data.index = data.loc[:,'Region']
    data = data.loc[:,'2018']
    data = data.iloc[:-2]
    data.columns = data_files[i][:-4]
    features.append(data)