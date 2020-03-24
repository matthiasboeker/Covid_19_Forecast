#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 13:30:38 2020

@author: matthiasboeker
Update"""

NO = country_filter(Country='Norway')
DE = country_filter(Country='Germany')
AU = country_filter(Country='Austria')
IT = country_filter(Country='Italy')
SW = country_filter(Country='Sweden')
GB = country_filter(Country='United Kingdom')
FR = country_filter(Country='France')
SP = country_filter(Country='Spain')


#New infections
fig, ax = plt.subplots()
np.log(NO.loc[:,'Infected']).diff().iloc[1:].plot()
np.log(DE.loc[:,'Infected']).diff().iloc[1:].plot()
np.log(AU.loc[:,'Infected']).diff().iloc[1:].plot()
np.log(IT.loc[:,'Infected']).diff().iloc[1:].plot()
np.log(SW.loc[:,'Infected']).diff().iloc[1:].plot()
np.log(GB.loc[GB['Province/State']=='United Kingdom','Infected']).diff().iloc[1:].plot()
np.log(FR.loc[FR['Province/State']=='France','Infected']).diff().iloc[1:].plot()
np.log(SP.loc[SP['Province/State']=='Spain','Infected']).diff().iloc[1:].plot()
ax.legend(['Norway','Germany','Austria','Italy','Sweden','United Kingdom','France','Spain'])
ax.set_ylabel('New_Infections')


#Deaths
fig, ax = plt.subplots()
NO.loc[:,'Deaths'].diff().iloc[1:].plot()
DE.loc[:,'Deaths'].diff().iloc[1:].plot()
AU.loc[:,'Deaths'].diff().iloc[1:].plot()
IT.loc[:,'Deaths'].diff().iloc[1:].plot()
SW.loc[:,'Deaths'].diff().iloc[1:].plot()
GB.loc[GB['Province/State']=='United Kingdom','Deaths'].diff().iloc[1:].plot()
FR.loc[FR['Province/State']=='France','Deaths'].diff().iloc[1:].plot()
SP.loc[SP['Province/State']=='Spain','Deaths'].diff().iloc[1:].plot()
ax.legend(['Norway','Germany','Austria','Italy','Sweden','United Kingdom','France','Spain'])
ax.set_ylabel('Deaths')