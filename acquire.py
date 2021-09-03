import pandas as pd
import numpy as np
import os
import requests

#acquire
#from env import host, user, password
from pydataset import data


# turn off pink warning boxes
import warnings
warnings.filterwarnings("ignore")


# get helper function to get the necessary connction to url.

# def get_connection(db, user=user, host=host, password=password):
#     '''
#     This function uses my info from my env file to create a connection urs to access database info.
#     '''
#     return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    

def get_df():
    '''
    returns Water Potability data into a csv, and creates it for you
    '''
    if os.path.isfile('water_potability.csv'):
        df = pd.read_csv('water_potability.csv', index_col=0)
        return df
