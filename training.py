'''
This script trains an ML model using ingested data files. Saves model as a pickle file.

Author: Femi Bolarinwa
Date: May 2023
'''

#importing needed python libraries
import pandas as pd
import numpy as np
import pickle
import os
#from sklearn import metrics
#from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import json

##Load config.json and get path variables
with open('config.json','r') as f:
    config = json.load(f) 

dataset_csv_path = os.path.join(config['output_folder_path']) 
model_path = os.path.join(config['output_model_path']) 


#Function for training the model
def train_model():
    '''
    trains an ML model using ingested data files.
    Input:

    Returns:

    '''
    
    #logistic regression for training
    logit = LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                    intercept_scaling=1, l1_ratio=None, max_iter=100,
                    multi_class='auto', n_jobs=None, penalty='l2',
                    random_state=0, solver='liblinear', tol=0.0001, verbose=0,
                    warm_start=False)
    
    #reading in training data
    df = pd.read_csv(dataset_csv_path+'/finaldata.csv')
    df.drop(columns = ['corporation'], inplace=True) #'Unnamed: 0',
    y = df.pop('exited')
    X = df

    #fit the logistic regression to data
    model = logit.fit(X, y)

    isExist = os.path.exists(model_path)
    if not isExist:
        os.makedirs(model_path)
    
    #write the trained model to your workspace in a file called trainedmodel.pkl
    pickle.dump(model, open('./' + model_path + '/trainedmodel.pkl', 'wb'))


if __name__ == '__main__':
    train_model()
