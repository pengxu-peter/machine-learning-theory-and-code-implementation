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
    def __init__(self,node_num,active_mode):
        self.node_num = node_num
        self.active_mode = active_mode
        
        self.weight = np.random.rand(self.node_num,self.pre_layer.node_num)
        self.pre_layer.set_post_layer(self)
        
        
    def set_post_layer(self, post_layer):
        self.post_layer = post_layer
    

class Layer(object):
    def __init__(self, **kwargs):
        allowed_kwargs = {'input_shape',
                          'batch_input_shape',
                          'batch_size',
                          'dtype',
                          'name',
                          'trainable',
                          'weights',
                          'input_dtype',  # legacy
                          }
        for kwarg in kwargs:
            if kwarg not in allowed_kwargs:
                raise TypeError('Keyword argument not understood:', kwarg)
        name = kwargs.get('name')
        if not name:
            prefix = self.__class__.__name__
            name = _to_snake_case(prefix) + '_' + str(K.get_uid(prefix))
        self.name = name

class Dense(Layer):
    def __init__(self, filters, name):
        self.pre_layer = pre_layer
        self.node_num = node_num
        self.active_mode = active_mode
        
        self.weight = np.random.rand(self.node_num,self.pre_layer.node_num)
        self.pre_layer.set_post_layer(self)
        
        
    def __call__(self, inputs, **kwargs):
        self.post_layer = post_layer
    
    
    

