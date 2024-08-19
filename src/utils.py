# Utility functions

import pandas as pd
import numpy as np

def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv("../data/raw.csv")

def clean_data(df):
    """Clean the DataFrame by handling missing values and duplicates."""
    df = df.drop_duplicates()
    df = df.fillna(method='ffill')
    return df

def normalize_data(df):
    """Normalize numerical features in the DataFrame."""
    return (df - df.mean()) / df.std()

def plot_feature_distribution(df, feature):
    """Plot the distribution of a feature."""
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    df[feature].hist(bins=30)
    plt.title(f'Distribution of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Frequency')
    plt.show()