# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 16:41:56 2018

@author:Onkar Mumbrekar

Website: www.onkarmumbrekar.co.in
"""
import numpy as np
#def Prediction(user,item,w,userdata,p,sources):
#    ri_dash = cal_rating_mean_ri_dash(userdata,item)
#    #print("ri_dash ", ri_dash)
#    sigma_i = cal_variance(userdata,item)
#    n=(p-1)*sources
#    numerator = cal_numerator(user,item,userdata,w,n)
#    denominator =  cal_denominator(item,w,n)
#    intermediatedata =numerator/denominator
#    prediction_i = ri_dash + (sigma_i * intermediatedata)
#    return prediction_i


def Prediction(user,w,userdata,p,sources):
    prediction_user = np.zeros(4)
    start = (p-1)*sources
    end = (p*sources)
    for item in range(start,end):
        ri_dash = cal_rating_mean_ri_dash(userdata,item)
        sigma_i = cal_variance(userdata,item)
        n=(p-1)*sources
        numerator = cal_numerator(user,item,userdata,w,n)
        denominator =  cal_denominator(item,w,n)
        intermediatedata =numerator/denominator
        prediction_user[item-((p-1)*sources)] = ri_dash + (sigma_i * intermediatedata)
    return prediction_user
        

    
def cal_rating_mean_ri_dash(userdata,item):
    r_dash = userdata.mean(axis=0)[item]
    return r_dash

def cal_variance(userdata,item):
    sigma =userdata.var(axis=0)[item]
    return sigma

def cal_numerator(user,item,userdata,w,n):
    numerator=0
    for j in range(n-1):
        ruj = userdata[user,j]
        rj_dash = cal_rating_mean_ri_dash(userdata,j)
        sigma_j =cal_variance(userdata,j)
        wij = w[item,j]
        numerator += ((ruj-rj_dash)/sigma_j)*wij
    return numerator
    
def cal_denominator(item,w,n):
    wij_sum = w[item,:n-1].sum()
    return wij_sum
   
    