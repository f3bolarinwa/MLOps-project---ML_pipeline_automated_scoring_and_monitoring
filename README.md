# Project: Automating ML Model Pipeline

A program requirement for Machine Learning DevOps Engineer Nanodegree @ Udacity School of Artificial Intelligence

## Project Description

In this project, I built a dynamic risk assessment system to predict client attrition for a company. I created a system for continuous data ingestion, model scoring and drift assessment, model re-training and re-deployment. I ensured continuous model monitoring and reporting with API, ML diagnostics for latency, dependency, data integrity and stability issues. I automated the entire ML pipeline using Cronjob to ensure minimal manual intervention.

## Repository Content Description

Overview of the content in repository:

1)source_data: directory contains data in csv files for model training

2)model: directory contains ML model in pickle format accompanied by model performance metrics info

3)ingested_data: aggregation of ingested data used to train current model accompanied by record of ingested datafiles

4)test_data: contains test data to used for model performance assessment

5)production_deployment: contains production-ready model accompanied by model performance metrics info

6)config.json: json file for directory management

7)ingestion.py: script for data ingestion and record keeping

8)training.py: script for ML model re-training

9)scoring.py: script for model scoring against testdata

10)deployment.py: copies production-ready model into production_deployment

11)diagnostics.py: script runs diagnostics like data summary stats, training time, data ingestion time, data integrity and stability checks, list outdated software modules in the environment

12)reporting.py: script to run a test prediction with the deployed model and
generates a confusion matrix plot

13)apicalls.py: script to call API endpoints and write responses to a text file. 

14)app.py: script to sets up API (using flask framework) to easily access ML diagnostics and model prediction results.

15)fullprocess.py: script automates the entire pipeline process of data ingestion, model training, scoring, monitoring, deployement and diagnostics

16)cronjob.txt: contains cronjob to run fullprocess.py (entire ML pipeline process) every 10 minutes.

17)requirements.txt: contains list of dependencies to run pipeline


## Running Files

1)Clone git repository to local machine

2)Install dependencies by running command:

> pip install -r requirements.txt

3)Run diagnostics:

>python diagnostics.py

4)Launch API locally by running command:

> python app.py

5)Call API endpoints by running:

> python apicalls.py

