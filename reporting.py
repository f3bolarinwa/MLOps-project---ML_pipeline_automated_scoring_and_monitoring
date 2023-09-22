'''
This script runs a test prediction with the deployed model and
generates a confusion matrix plot

Author: Femi Bolarinwa
Date: May 2023
'''

#importing needed python libraries
import pickle
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os

from diagnostics import model_predictions
from sklearn.metrics import confusion_matrix


#Load config.json and get path variables
with open('config.json','r') as f:
    config = json.load(f) 

dataset_csv_path = os.path.join(config['output_folder_path']) 
test_data_path = os.path.join(config['test_data_path']) 
model_path = os.path.join(config['output_model_path']) 


#Function for reporting
def score_model():
    '''
    calculates a confusion matrix using the test data and the deployed model
    Input:   
    df: file path
        test data
    
    Returns: 
    predictions: nd.array
        predictions
    '''

    predictions = model_predictions()


    data = pd.read_csv(test_data_path+'/testdata.csv')
   
    data.drop(columns = ['corporation'], inplace=True)
    y = data.pop('exited')

    cm=confusion_matrix(y, predictions)

    plt.figure(figsize=(5, 5))
    sns.heatmap(cm, annot = True,  fmt = '.0f')
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.title('Confusion Matrix')
    plt.savefig(model_path+'/confusionmatrix.png')

if __name__ == '__main__':
    score_model()
