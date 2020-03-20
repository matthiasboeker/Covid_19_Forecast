#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:00:13 2020

@author: matthiasboeker
Visualizing data in China"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


CH= country_filter(Country='China')

state_list = CH['Province/State'].drop_duplicates()

#Calculate the distance to Hubei 
CH['Distance'] = np.square(np.power(CH['Long']-CH.loc[CH['Province/State']=='Hubei','Long'],2)+np.power(CH['Lat']-CH.loc[CH['Province/State']=='Hubei','Lat'],2))

#Classify states according to their distance 
close_states = CH.sort_values('Distance')['Province/State'].drop_duplicates()[:6]
mid_close = states= CH.sort_values('Distance')['Province/State'].drop_duplicates()[6:12]
middle_states = CH.sort_values('Distance')['Province/State'].drop_duplicates()[12:19]
mid_far_states = CH.sort_values('Distance')['Province/State'].drop_duplicates()[19:26]
far_states = CH.sort_values('Distance')['Province/State'].drop_duplicates()[26:]

#Plot New Infections per Day for the different classes 
fig, ax = plt.subplots()
for state in close_states:
    CH.loc[CH['Province/State']==state,'Infected'].diff().rolling(window=2).mean().iloc[2:].transform(lambda x: x*(100/x.max())).plot()
ax.legend(close_states)

fig, ax = plt.subplots()
for state in mid_close:
    CH.loc[CH['Province/State']==state,'Infected'].diff().rolling(window=2).mean().iloc[2:].transform(lambda x: x*(100/x.max())).plot()
ax.legend(mid_close)

fig, ax = plt.subplots()
for state in middle_states:
    CH.loc[CH['Province/State']==state,'Infected'].diff().rolling(window=2).mean().iloc[2:].transform(lambda x: x*(100/x.max())).plot()
ax.legend(middle_states)

fig, ax = plt.subplots()
for state in mid_far_states:
    CH.loc[CH['Province/State']==state,'Infected'].diff().rolling(window=2).mean().iloc[2:].transform(lambda x: x*(100/x.max())).plot()
ax.legend(mid_far_states)

fig, ax = plt.subplots()
for state in far_states:
    CH.loc[CH['Province/State']==state,'Infected'].diff().rolling(window=2).mean().iloc[2:].transform(lambda x: x*(100/x.max())).plot()
ax.legend(far_states)

