# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 11:05:26 2018

@author: Onkar Mumbrekar

Website: www.onkarmumbrekar.co.in
"""

from scipy.spatial.distance import pdist, squareform
from dataClean import userCreation

def similarityMatrixCreation(P,sources,userdata):# P=user size, sources = temperature, humidity, light, voltage
    M = userCreation(P,sources,userdata) 
    M_u = M.mean(axis=1)
    item_mean_subtracted = M - M_u[:, None]
    w =1-squareform(pdist(item_mean_subtracted.T, 'cosine'))
    return w
