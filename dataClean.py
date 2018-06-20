# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 09:36:45 2018

@author:Onkar Mumbrekar

Website: www.onkarmumbrekar.co.in
"""

import numpy as np

def userCreation(P,sources,userdata):
    users = np.zeros((len(userdata.iloc[:])-P, P*sources))
    for i in range(len(userdata.iloc[:])-P):
        users[i]=np.array(userdata.iloc[i:i+P]).reshape(1,P*sources)
    return users

def cleanDataset(userdata,colname):
    userdata = userdata.dropna() #remove rows with null values
    userdata = remove_outlier(userdata,'temperature')
    return userdata

def remove_outlier(df_in, col_name):# remove extreme values
    q1 = df_in[col_name].quantile(0.25)
    q3 = df_in[col_name].quantile(0.75)
    iqr = q3-q1 
    fence_low  = q1-1.5*iqr
    fence_high = q3+1.5*iqr
    df_out = df_in.loc[(df_in[col_name] > fence_low) & (df_in[col_name] < fence_high)]
    return df_out


