
def log_mod_one(data_df):

    # Define the threshold for high-status schools
    threshold = 50
    data_df['High_Status_School'] = data_df['RepecRank'] <= threshold

    # Define the binary outcome (1 if NoPPubGrad == 0, else 0)
    data_df['ZeroPubs'] = data_df['NoPPubGrad'] == 0

    # Check data types and convert if necessary
    data_df['High_Status_School'] = data_df['High_Status_School'].astype(int)
    data_df['ZeroPubs'] = data_df['ZeroPubs'].astype(int)
    data_df['TotalYearPhD'] = pd.to_numeric(data_df['TotalYearPhD'], errors='coerce')

    # Ensure there are no missing values
    data_df = data_df.dropna(subset=['High_Status_School', 'ZeroPubs', 'TotalYearPhD'])

    # Define the predictor variables
    X = data_df[['High_Status_School', 'TotalYearPhD']]
    X = sm.add_constant(X)  # Adds a constant term to the predictor

    # Define the outcome variable
    y = data_df['ZeroPubs']

    # Fit the logistic regression model
    logit_model = sm.Logit(y, X)
    result = logit_model.fit()

    # Print the summary of the logistic regression
    print(result.summary())

import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

if __name__ == "__main__":

    print('should not run directly')