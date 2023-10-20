import pandas as pd
from scikit-learn.metrics import accuracy_score
from scikit-learn.ensemble import RandomForestClassifier
from scikit-learn.model_selection import train_test_split
import pickle

penguin_df = pd.read_csv(
    r"/workspaces/ughhhh/streamlit-app/penguin_ml/penguins.csv")
penguin_df.dropna(inplace=True)
output = penguin_df['species']
features = penguin_df[['island', 'bill_length_mm', 'bill_depth_mm', 
                      'flipper_length_mm', 'body_mass_g', 'sex']]
features = pd.get_dummies(features)
output, uniques = pd.factorize(output)
x_tr