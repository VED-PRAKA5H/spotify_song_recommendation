 # Data preprocessing functions
# data_preprocessing.py now lets start with feature engineering 

import pandas as pd

def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv('../data/spotify.csv')

def clean_data(df):
    """Clean the DataFrame by handling missing values."""
    df.dropna(subset=['track_name'], inplace=True)
    return df

def feature_engineering(df):
    """Perform feature engineering on the DataFrame."""
    list_of_keys = df['key'].unique()
    for i in range(len(list_of_keys)):
        df.loc[df.key == list_of_keys[i], 'key'] = i
    return df


