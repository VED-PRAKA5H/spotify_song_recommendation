 # Model definition and training functions

# model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score

def train_model(df):
    features = ['track_popularity', 'danceability', 'energy', 'key', 'loudness', 
                'mode', 'speechiness', 'acousticness', 'instrumentalness', 
                'liveness', 'valence', 'tempo', 'duration_ms']
    
    y = df.track_popularity
    X = df[features]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    auc = roc_auc_score(y_test, predictions)
    
    print('Accuracy:', accuracy)
    print('AUC:', auc)