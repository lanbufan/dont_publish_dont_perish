def threshold_var(data_df):

    # Define different thresholds for high-status schools
    thresholds = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

    results = []
    group_sizes = []

    for threshold in thresholds:
        # Create a new column to indicate if the school is high-status
        data_df['High_Status_School'] = data_df['RepecRank'] <= threshold

        # Create a contingency table
        contingency_table = pd.crosstab(data_df['High_Status_School'], data_df['NoPPubGrad'])

        # Perform the chi-square test
        chi2, p, dof, expected = chi2_contingency(contingency_table)

        # Append results
        results.append((threshold, chi2, p))
        high_status_size = data_df['High_Status_School'].sum()
        low_status_size = len(data_df) - high_status_size
        group_sizes.append((threshold, high_status_size, low_status_size))

        # Print intermediate results for debugging
        print(f"Threshold: {threshold}, High Status Size: {high_status_size}, Low Status Size: {low_status_size}")

    # Convert results to DataFrames for better visualization
    results_df = pd.DataFrame(results, columns=['Threshold', 'Chi2', 'P-value'])
    group_sizes_df = pd.DataFrame(group_sizes, columns=['Threshold', 'High_Status_Size', 'Low_Status_Size'])

    # Plot P-value vs. Threshold
    plt.figure(figsize=(12, 6))
    plt.plot(results_df['Threshold'], results_df['P-value'], marker='o', linestyle='-', color='b')
    plt.axhline(y=0.05, color='r', linestyle='--', label='Significance Level (0.05)')
    plt.title('P-value vs. Threshold for High-Status Schools')
    plt.xlabel('Rank Threshold')
    plt.ylabel('P-value')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot group sizes vs. Threshold
    plt.figure(figsize=(12, 6))
    plt.plot(group_sizes_df['Threshold'], group_sizes_df['High_Status_Size'], marker='o', linestyle='-', color='g', label='High Status Size')
    plt.plot(group_sizes_df['Threshold'], group_sizes_df['Low_Status_Size'], marker='o', linestyle='-', color='orange', label='Low Status Size')
    plt.title('Group Sizes vs. Threshold for High-Status Schools')
    plt.xlabel('Rank Threshold')
    plt.ylabel('Group Size')
    plt.legend()
    plt.grid(True)
    plt.show()

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

# Load the provided CSV file
# data_path = 'dpdp_economics_master_rank.csv'
data_path = 'dpdp_economics_master_rank_name.csv'

data_df = pd.read_csv(data_path)

# Calculate the proportion of economists with 0 publications by PhD graduation year
total_economists = len(data_df)
economists_with_zero_pubs = len(data_df[data_df['NoPPubGrad'] == 0])
proportion_zero_pubs = economists_with_zero_pubs / total_economists

print(f"Total number of economists: {total_economists}")
print(f"Number of economists with 0 publications by PhD graduation year: {economists_with_zero_pubs}")
print(f"Proportion of economists with 0 publications by PhD graduation year: {proportion_zero_pubs:.4f}")

######################
# FEATURES ENGINEERING
######################

from features import get_gender, get_ethn

# GENDER
data_df = get_gender(data_df)

# Convert Gender to binary: Male = 0, Female = 1
data_df['GenderBinary'] = data_df['Gender'].map({'Male': 0, 'Female': 1})

print('gender')
dev_log = input()

from ethnicolr import pred_fl_reg_ln, pred_fl_reg_name

data_df = get_ethn(data_df)
print('eth')
dev_log = input()

######################
# PREDICTIVE MODEL
######################

from logistic_regression import log_mod_one

log_mod_one(data_df)
dev_log = input()

threshold_var(data_df)

# Define a threshold for high-status schools (e.g., top 50)
high_status_threshold = 50

# Create a new column to indicate if the school is high-status
data_df['High_Status_School'] = data_df['RepecRank'] <= high_status_threshold

# Create a contingency table
contingency_table = pd.crosstab(data_df['High_Status_School'], data_df['NoPPubGrad'])

# Perform the chi-square test
chi2, p, dof, expected = chi2_contingency(contingency_table)

# Display the results
print("Contingency Table:")
print(contingency_table)
print("\nChi-Square Test:")
print(f"Chi2: {chi2}")
print(f"P-value: {p}")
print(f"Degrees of Freedom: {dof}")
print("Expected Frequencies:")
print(expected)

# Save the contingency table to a CSV file for review
contingency_table_output = 'contingency_table.csv'
contingency_table.to_csv(contingency_table_output)

# save df
data_path = 'dpdp_economics_master_rank_name_gender_race.csv'
data_df.to_csv(data_path, index=False)
