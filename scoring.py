'''
This script scores a trained ML model using testdata.
Writes the score (f1-score) to a text file. 

Author: Femi Bolarinwa
Date: May 2023
'''

#importing needed python libraries
import pandas as pd
import numpy as np
import pickle
import os
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import json


#Load config.json and get path variables
with open('config.json','r') as f:
    config = json.load(f) 

dataset_csv_path = os.path.join(config['output_folder_path']) 
test_data_path = os.path.join(config['test_data_path']) 
model_path = os.path.join(config['output_model_path']) 

#Function for model scoring
def score_model(df = test_data_path+'/testdata.csv', path = model_path):
    '''
    Takes a trained model, load test data, and calculate an F1 score 
    Input:   
    df: dataframe
        training data
    path: file path
        path to saved model

    Returns: 
    f1score: float
        performance metric
    '''

    #locate trained model
    with open(os.getcwd() +'/' + path + '/trainedmodel.pkl', 'rb') as file: #os.getcwd() +'/' + 
        model = pickle.load(file)

    #read test data
    df = pd.read_csv(df)
    df.drop(columns = ['corporation'], inplace=True)
    y = df.pop('exited')
    X = df

    #make prediction and score
    predictions = model.predict(X)
    f1score = metrics.f1_score(predictions,y)

    #write score to a text file
    MyFile=open(path+'/latestscore.txt','w')
    MyFile.write(str(f1score) + '\n')

    return f1score


if __name__ == '__main__':
    score_model()