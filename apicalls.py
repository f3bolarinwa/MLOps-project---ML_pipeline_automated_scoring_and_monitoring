'''
This script calls API endpoints and write responses to a text file. 

Author: Femi Bolarinwa
Date: May 2023
'''

#importing needed python libraries
import requests
import json
import subprocess
import os

#Specify a URL that resolves to your workspace
URL = "http://127.0.0.1/8000"


# Load config.json and get environment variables
with open('config.json', 'r') as f:
    config = json.load(f)
test_data_path = config['test_data_path']+ "/testdata.csv"
model_dir = config["output_model_path"]
data = {"data_path": test_data_path}



#Calls each API endpoint and store the responses
#response1 = requests.post(URL + "prediction", json=data).json() #content #put an API call here
#response1 = requests.post(URL+'/prediction?filename=./testdata/testdata.csv').content
response1=subprocess.run(['curl', '127.0.0.1:8000/prediction?filename=./testdata/testdata.csv'],capture_output=True).stdout
response2=subprocess.run(['curl', '127.0.0.1:8000/scoring?'],capture_output=True).stdout
response3=subprocess.run(['curl', '127.0.0.1:8000/summarystats?'],capture_output=True).stdout
response4=subprocess.run(['curl', '127.0.0.1:8000/missingdata?'],capture_output=True).stdout
response5=subprocess.run(['curl', '127.0.0.1:8000/executiontime?'],capture_output=True).stdout
response6=subprocess.run(['curl', '127.0.0.1:8000/outdatedpackages?'],capture_output=True).stdout

 #curl '127.0.0.1:8000/prediction?filename=./testdata/testdata.csv'
#response2 = #put an API call here
#response3 = #put an API call here
#response4 = #put an API call here

#combine all API responses
#responses = #combine reponses here

#write the responses to your workspace

print(response1)#.replace('\n','') for i in response1)
print(response2)
print(response3)
print(response4)
print(response5)
print(response6)

#write the responses to a txt file
MyFile=open(model_dir+'/apireturns.txt','w')
MyFile.write(str(response1) + '\n')
MyFile.write(str(response2) + '\n')
MyFile.write(str(response3) + '\n')
MyFile.write(str(response4) + '\n')
MyFile.write(str(response5) + '\n')

#for element in response6:
#        MyFile.write(str(element) + '\n')

MyFile.write(str(response6) + '\n')