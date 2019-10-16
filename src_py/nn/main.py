# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 07:54:08 2019
main function
@author: xupeng
"""
from sklearn import datasets
import numpy as np
import random as rn
import copy
np.random.seed(1)
rn.seed(1)

from layer.layer import layer


def data_get():
    # get dataset
    n_samples = 1000
    (data,label) = datasets.make_moons(n_samples=n_samples, noise=.15)
    #plt.scatter(data[:,0],data[:,1],c=label)
    data_list_shuffer = list(np.arange(n_samples))
    rn.shuffle(data_list_shuffer)
    train_ratio,val_ratio,test_ratio = 0.7,0.2,0.1
    train_data,train_label = data[data_list_shuffer[0:int(n_samples*train_ratio)]],label[data_list_shuffer[0:int(n_samples*train_ratio)]]
    val_data,val_label = data[data_list_shuffer[int(n_samples*train_ratio):int(n_samples*(train_ratio+val_ratio))]],label[data_list_shuffer[int(n_samples*train_ratio):int(n_samples*(train_ratio+val_ratio))]]
    test_data,test_label = data[data_list_shuffer[int(n_samples*(train_ratio+val_ratio)):]],label[data_list_shuffer[int(n_samples*(train_ratio+val_ratio)):]]
    #plt.scatter(val_data[:,0],val_data[:,1],c=val_label)
    return train_data,train_label,val_data,val_label,test_data,test_label
    

def main():
    train_data,train_label,val_data,val_label,test_data,test_label = data_get()
    
    Input = 
    
    
    
    




