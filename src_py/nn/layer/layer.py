# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 07:31:32 2019
layer
@author: xupeng
"""
import numpy as np
import random as rn
import copy

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

class Input():
    def __init__(self,filters):
        self.filters = filters

    def set_post_layer(self, outputs):
        self.post_layer = outputs
    

class Layer(object):
    def __init__(self, name='default', trainable=True, weights=None):
        self.name = name

class Dense(Layer):
    def __init__(self, filters, **kwargs):
        self.filters = filters
        
    def __call__(self, inputs, **kwargs):
        self.pre_layer = inputs
        self.weight = np.random.rand(self.filters, self.pre_layer.filters)
        self.pre_layer.set_post_layer(self)

    def set_post_layer(self, outputs):             
        # used for get the relation of all layer
        self.post_layer = outputs
        
class Model():
    def __init__(self, input, output):
        self.input = input
        self.output = output
        temp_layer = copy.deepcopy(input)
        self.layer_list = []
        while(temp_layer is not self.output):
            temp_layer = copy.deepcopy(temp_layer.post_layer)
            self.layer_list.append(temp_layer)


    
    

