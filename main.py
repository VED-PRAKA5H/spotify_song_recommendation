# Importing the utils module
# from src.utils import load_data, clean_data, plot_feature_distribution

# # Load data
# data = load_data('data/processed/song_data.csv')

# # Clean data
# cleaned_data = clean_data(data)

# # Plot feature distribution
# plot_feature_distribution(cleaned_data, 'danceability')



import pandas as pd
from src.data_preprocessing import load_data, clean_data, feature_engineering
from src.model import train_model

# Load and preprocess data
df = load_data("data/spotify.csv")
df = clean_data(df)
df = feature_engineering(df)

# Train model
train_model(df)