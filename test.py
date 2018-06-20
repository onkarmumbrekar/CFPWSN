# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 09:54:37 2018

@author:Onkar Mumbrekar

Website: www.onkarmumbrekar.co.in
"""

import pandas as pd
from scipy.spatial.distance import pdist, squareform
from sklearn.model_selection import train_test_split
import numpy as np
import Prediction_model as pm

data_file = 'data.csv'

dataset = pd.read_csv(data_file,parse_dates=[['date','time']],index_col=0)
dataset = pd.DataFrame(dataset,columns=['temperature','humidity','light','voltage'])
dataset.dropna()
dataset.to_csv('geo.csv')

train_data, test_data = train_test_split(dataset, test_size = 0.20, random_state=0)

P=4
users = np.zeros((len(train_data.iloc[:])-P, P*4))
for i in range(len(train_data.iloc[:])-P):
   users[i]=np.array(train_data.iloc[i:i+P]).reshape(1,P*4)


M = users

M_u = M.mean(axis=1)
item_mean_subtracted = M - M_u[:, None]


w =1-squareform(pdist(item_mean_subtracted.T, 'cosine'))


prediction = pm.Prediction(item=12,p=4,sources=4,user=3,userdata=users,w=w)
print(prediction)