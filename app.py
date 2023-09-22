'''
This script sets up an API (using flask framework) to easily access ML diagnostics and model prediction results.

Author: Femi Bolarinwa
Date: May 2023
'''

#importing needed python libraries
from flask import Flask, session, jsonify, request
import pandas as pd
import numpy as np
import pickle
#import create_prediction_model
#import diagnosis 
#import predict_exited_from_saved_model
import json
import os

from diagnostics import model_predictions, dataframe_summary, missing_data, execution_time, outdated_packages_list
from scoring import score_model


#Set up variables
app = Flask(__name__)
app.secret_key = '1652d576-484a-49fd-913a-6879acfa6ba4'

with open('config.json','r') as f:
    config = json.load(f) 

dataset_csv_path = os.path.join(config['output_folder_path'])
model_path = os.path.join(config['output_model_path'])  


with open(model_path + '/trainedmodel.pkl', 'rb') as file:
        model = pickle.load(file)

prediction_model = model #None

def readpandas(filename):
    thedata=pd.read_csv(filename)
    return thedata

#Prediction Endpoint
@app.route("/prediction")#, methods=['POST','OPTIONS'])
def predict():        
    '''
    calls the prediction function you created in diagnostics.py
    '''

    #if request.method=='POST':

    filename = request.args.get('filename')
    predictions = model_predictions(df = filename)

    return {'predictions': str(predictions)}


#Scoring Endpoint
@app.route("/scoring")#, methods=['GET','OPTIONS'])
def stats():        
    '''
    check the score of the deployed model
    '''

    #if request.method=='GET':
    f1score = score_model()

    return {'f1score': str(f1score)}


#Summary Statistics Endpoint
@app.route("/summarystats")#, methods=['GET','OPTIONS'])
def stats_1():        
    '''
    check means, medians, and modes for each column
    '''
    
    #if request.method=='GET':
    summary_stat = dataframe_summary()

    return str(summary_stat)

    
#Diagnostics Endpoints
@app.route("/missingdata")#, methods=['GET','OPTIONS'])
def stats_2():  
    '''
    check missing values for each column
    '''

    napercents = missing_data()
    return str(napercents)

@app.route("/executiontime")#, methods=['GET','OPTIONS'])
def stats_3(): 
    '''
    check execution time for ingesting and model training
    '''
       
    times = execution_time()
    return str(times)

@app.route("/outdatedpackages")#, methods=['GET','OPTIONS'])
def stats_4():    
    '''
    check outdate dependencies
    '''
           
    outdated_packages = outdated_packages_list()
    return (outdated_packages)



if __name__ == "__main__":    
    app.run(host='0.0.0.0', port=8000, debug=True, threaded=True)
