'''
This script ingest data files into python and writes them to an output file.
Also keeps record of ingested data files

Author: Femi Bolarinwa
Date: May 2023
'''

#importing needed python libraries
import pandas as pd
import numpy as np
import os
import json
from datetime import datetime


#Loads config.json and get input and output paths
with open('config.json','r') as f:
    config = json.load(f) 

input_folder_path = config['input_folder_path']
output_folder_path = config['output_folder_path']



#Function for data ingestion
def merge_multiple_dataframe():
    '''
    locates data file paths and merges them into a single file
    Input:

    Returns:
    
    '''
    #initialize list to hold file names
    records = []

    #initialize dataframe for merged datafile
    final_dataframe = pd.DataFrame(columns=['corporation','lastmonth_activity',	
                        'lastyear_activity','number_of_employees','exited'])

    #get current time
    dateTimeObj=datetime.now()
    thetimenow=str(dateTimeObj.year)+ '/'+str(dateTimeObj.month)+ '/'+str(dateTimeObj.day)

    #locate files and merge them
    directory = input_folder_path 
    filenames = os.listdir(os.getcwd()+'/'+directory)
    for each_filename in filenames:
        csv_path = os.getcwd()+'/'+directory+'/'+each_filename
        currentdf = pd.read_csv(csv_path, encoding = "utf-8",index_col=False)
       
        final_dataframe = pd.concat([final_dataframe, currentdf], ignore_index=True)
        final_dataframe = final_dataframe.drop_duplicates()

        records.append(each_filename)
            
    out_path = output_folder_path
    isExist = os.path.exists(out_path)
    if not isExist:
        os.makedirs(out_path)

    #write merged data to a csv and keep record in a txt file
    final_dataframe.to_csv(out_path+'/finaldata.csv', index=False)
    MyFile=open(out_path+'/'+'ingestedfiles.txt','w')
    for element in records:
        MyFile.write(str(element) + '\n')
    


if __name__ == '__main__':
    merge_multiple_dataframe()


