# Importing the utils module
from src.utils import load_data, clean_data, plot_feature_distribution

# Load data
data = load_data('data/processed/song_data.csv')

# Clean data
cleaned_data = clean_data(data)

# Plot feature distribution
plot_feature_distribution(cleaned_data, 'danceability')