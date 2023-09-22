'''
This script copies trained model, model score and info on training data
from developement directories into a production/deployment directory

Author: Femi Bolarinwa
Date: May 2023
'''

#importing needed python libraries
from flask import Flask, session, jsonify, request
import pandas as pd
import numpy as np
import pickle
import os
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import json

import shutil


#Load config.json and correct path variable
with open('config.json','r') as f:
    config = json.load(f) 

dataset_csv_path = os.path.join(config['output_folder_path']) 
prod_deployment_path = os.path.join(config['prod_deployment_path']) 
model_path = os.path.join(config['output_model_path']) 


#function for deployment
def store_model_into_pickle():#(model):
    '''
    copies trained model, model score and info on training data to production directory
    Input:   
    Returns: 
    '''

    isExist = os.path.exists(prod_deployment_path)
    if not isExist:
        os.makedirs(prod_deployment_path)

    shutil.copy(model_path+'/trainedmodel.pkl', prod_deployment_path)
    shutil.copy(model_path+'/latestscore.txt', prod_deployment_path)
    shutil.copy(dataset_csv_path +'/ingestedfiles.txt', prod_deployment_path)

if __name__ == '__main__':
    store_model_into_pickle()
