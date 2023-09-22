'''
This script runs diagnostics like data summary stats, training time, data ingestion time,
 data integrity and stability checks

Author: Femi Bolarinwa
Date: May 2023
'''

#importing needed python libraries
import pandas as pd
import numpy as np
import timeit
import os
import json

import subprocess
import pytest
import pickle

#Load config.json and get environment variables
with open('config.json','r') as f:
    config = json.load(f) 

#file paths
dataset_csv_path = os.path.join(config['output_folder_path']) 
test_data_path = os.path.join(config['test_data_path']) 
model_path = os.path.join(config['output_model_path']) 


#Function to get model predictions
def model_predictions(df = test_data_path+'/testdata.csv'):
    '''
    read the deployed model and a test dataset, calculate predictions
    Input:   
    df: file path
        test data
    
    Returns: 
    predictions: nd.array
        predictions
    '''

    with open(model_path + '/trainedmodel.pkl', 'rb') as file:
        model = pickle.load(file)

    data = pd.read_csv(df)
    data.drop(columns = ['corporation'], inplace=True)
    y = data.pop('exited')
    X = data

    predictions = model.predict(X)

    return predictions

#Function to get summary statistics
def dataframe_summary(df = os.getcwd() + '/'+ test_data_path+'/testdata.csv'):
    '''
    gets summary statistics
    Input:   
    df: file path
        test data
    
    Returns: 
    predictions: dict
        summary stats
    '''
    summary_stat = []

    data = pd.read_csv(df)
    data.drop(columns = ['corporation', 'exited'], inplace=True)

    themeans=list(data.mean())
    themedians=list(data.median())
    thestds=list(data.std())

    return {'column mean': themeans, 
            'column median': themedians, 
            'column std': thestds}


def missing_data(df = os.getcwd() +'/' + test_data_path+'/testdata.csv'):
    '''
    does data integrity checks
    Input:   
    df: file path
        test data
    
    Returns: 
    predictions: dict
        missing data percentage
    '''

    data = pd.read_csv(df)
    nas=list(data.isna().sum())
    napercents=[nas[i]/len(data.index) for i in range(len(nas))]
    
    return {'column NA %': napercents}


#Function to get timings
def execution_time():
    '''
    #calculate execution time of training.py and ingestion.py
    Input: 

    Returns: 
    predictions: dict
       execution times
    '''

    starttime = timeit.default_timer()
    os.system('python training.py')
    train_time=timeit.default_timer() - starttime

    starttime = timeit.default_timer()
    os.system('python ingestion.py')
    ing_time=timeit.default_timer() - starttime

    return {'ingestion time':ing_time, 'training time': train_time}

#Function to check dependencies
def outdated_packages_list():
    '''
    get a list of outdated dependencies
    Input: 

    Returns: 
    predictions: text
       outdated dependencies
    '''
    outdated_packages = subprocess.check_output(['pip', 'list', '--outdated']).decode(os.sys.stdout.encoding)
    outdated_packages = str(outdated_packages)
    return outdated_packages


if __name__ == '__main__':
    #df = test_df()
    print({'predictions': list(model_predictions())})
    print(dataframe_summary())
    print(missing_data())
    print(execution_time())
    print(outdated_packages_list())


