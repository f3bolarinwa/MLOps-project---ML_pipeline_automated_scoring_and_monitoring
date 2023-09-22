'''
This script automates the entire pipeline process of data ingestion, 
model training, scoring, monitoring and deployement

Author: Femi Bolarinwa
Date: May 2023
'''

#importing needed python libraries
import training
import scoring
import deployment
import diagnostics
import reporting

import json
import os
import pickle
import pandas as pd
from sklearn import metrics

#Load config.json and correct path variable
with open('config.json','r') as f:
    config = json.load(f) 

deployment_folder_path = config['prod_deployment_path']
input_folder_path = config['input_folder_path']
ingesteddata_path = config['output_folder_path'] 
model_path = config['output_model_path'] #deployment_folder_path 

#Check data used to train model
with open(os.path.join(os.getcwd(), deployment_folder_path, 'ingestedfiles.txt'), 'r') as f:
    ingestedfiles = f.readlines()
ingestedfiles = [ingestedfile.replace('\n','') for ingestedfile in ingestedfiles]
print(ingestedfiles)


#Determine whether the source data folder has files that aren't listed in ingestedfiles.txt
filenames = os.listdir(os.getcwd()+'/'+input_folder_path)
print(filenames)

temp = []
for csv in filenames:
    if csv not in ingestedfiles:
        temp.append(csv)
 
print(temp)

#Deciding whether to proceed, part 1
#if it finds new data, it should proceed. otherwise, do end the process here
if temp:
    os.system('python ingestion.py')



#Checking for model drift
#check whether the score from the deployed model is different from the score from the model that uses the newest ingested data
    
    with open(os.path.join(os.getcwd(), deployment_folder_path, 'latestscore.txt'), 'r') as f:
        latestscore = f.read()#lines()
    #latestscore = [latestscore.replace('\n','') for ingestedfile in ingestedfiles]
    print(latestscore)
    f1score = scoring.score_model(df = ingesteddata_path+'/finaldata.csv', path = model_path) - .5
    print(f1score)
    

#Deciding whether to proceed, part 2
#if it finds model drift, you should proceed. otherwise, do end the process here
    if float(f1score) < float(latestscore):
        os.system('python training.py')
        
##Re-deployment
#if it finds evidence for model drift, re-run the deployment.py script
        os.system('python deployment.py')

#Diagnostics and reporting
#runs diagnostics.py and reporting.py for the re-deployed model
        os.system('python diagnostics.py')

        os.system('python apicalls.py') 
        
        os.system('python reporting.py') 
