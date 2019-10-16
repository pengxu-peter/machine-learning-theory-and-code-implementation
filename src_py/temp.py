# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 20:21:20 2019
@author: Administrator temp use
"""

import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
import random as rn
import copy
np.random.seed(1)
rn.seed(1)

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

# weights init
layer_nodes_list = [3,4,3,1] # the first layer num is len(data[0])
layer_nodes_list_all = [len(data[0])]+layer_nodes_list
W_list = [np.random.rand(layer_nodes_list_all[i],layer_nodes_list_all[i+1]) for i in range(len(layer_nodes_list))]
b_list = [np.zeros(layer_nodes_list[i]) for i in range(len(layer_nodes_list))]

def relu(z):
    z[z<0]=0
    return z
    
def relu_slop(z):
    slop=copy.deepcopy(z)
    slop[z<=0]=0
    slop[z>0]=1
    return slop

def sigmoid(z):
    return 1/(1+(np.e)**z)

# train process
learning_rate = 1e-1;
for iter_time in range(1000):
    # ----------- foreword ------------
    z_list=[]                         # before activation
    a_list = [train_data]             # after activation
    for i in range(len(layer_nodes_list)):
        z_list.append(a_list[i].dot(W_list[i])+b_list[i])
        if i != len(layer_nodes_list)-1:
            a_list.append(relu(z_list[i]))
        
    a_list.append(sigmoid(z_list[-1]))  # last be sigmoid
        
    # ----------- loss --------------
    loss = np.average(-train_label[:,np.newaxis]*np.log(a_list[-1])-(1-train_label[:,np.newaxis])*np.log(1-a_list[-1]))
    print('iter_time %d, loss: %.2f'%(iter_time,loss))
    
    # ----------- backword ------------
    dz_last = a_list[-1] - train_label[:,np.newaxis]     # sigmoid
    dz_reverse_list = [dz_last]
    dW_reverse_list = []
    db_reverse_list = []
    for i in range(len(layer_nodes_list)):
        dW_reverse_list.append((a_list[-i-2].T.dot(dz_reverse_list[i]))/len(train_label))
        db_reverse_list.append(np.sum(dz_reverse_list[i],axis=0)/len(train_label))
        if i != len(layer_nodes_list)-1:
            dz_reverse_list.append(dz_reverse_list[i].dot(W_list[-i-1].T)*relu_slop(z_list[-i-2]))
    
    # ----------- update weight -----------
    for i in range(len(layer_nodes_list)):
        W_list[i]+=learning_rate*dW_reverse_list[-i-1]
        b_list[i]+=learning_rate*db_reverse_list[-i-1]
    
    
    
    
    
    
    
    