import pandas as pd
import numpy as np
import os
import requests

def get_df():
    '''
    returns Water Potability data into a csv, and creates it for you
    '''
    if os.path.isfile('water_potability.csv'):
        df = pd.read_csv('water_potability.csv', index_col=0)
        return df
