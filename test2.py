# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 12:39:53 2018

@author: Onkar Mumbrekar

Website: www.onkarmumbrekar.co.in
"""

import pandas as pd
from Prediction_model import Prediction
from dataClean import cleanDataset,userCreation
from buildModel import similarityMatrixCreation

data_file = 'data.csv'

#dataset = pd.read_csv(data_file,parse_dates=[['date','time']],sep=' ',index_col=0)
dataset = pd.read_csv(data_file,parse_dates=[['date','time']],index_col=0)
dataset = pd.DataFrame(dataset,columns=['temperature','humidity','light','voltage'])
dataset = cleanDataset(dataset,'temperature')
p=10
users=userCreation(p,4,dataset)
w = similarityMatrixCreation(p,4,dataset)
for t in range(10):
    prd = Prediction(t,w,users,p,4)
    print(prd)



