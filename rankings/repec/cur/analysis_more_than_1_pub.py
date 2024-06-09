
import pandas as pd
from scipy.stats import chi2_contingency
from statsmodels.stats.proportion import proportions_ztest
import matplotlib.pyplot as plt
import numpy as np

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

    # Convert results to DataFrames for better visualization
    results_df = pd.DataFrame(results, columns=['Threshold', 'Chi2', 'P-value'])
    group_sizes_df = pd.DataFrame(group_sizes, columns=['Threshold', 'High_Status_Size', 'Low_Status_Size'])

    # Plot P-value vs. Threshold
    plt.figure(figsize=(12, 6))
    plt.plot(results_df['Threshold'], results_df['P-value'], marker='o', linestyle='-', color='b')
    plt.axhline(y=0.05, color='r', linestyle='--', label='Significance Level (0.05)')
    plt.title('P-value vs. Threshold for High-Status Schools (All Economists)')
    plt.xlabel('Rank Threshold')
    plt.ylabel('P-value')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot group sizes vs. Threshold
    plt.figure(figsize=(12, 6))
    plt.plot(group_sizes_df['Threshold'], group_sizes_df['High_Status_Size'], marker='o', linestyle='-', color='g', label='High Status Size')
    plt.plot(group_sizes_df['Threshold'], group_sizes_df['Low_Status_Size'], marker='o', linestyle='-', color='orange', label='Low Status Size')
    plt.title('Group Sizes vs. Threshold for High-Status Schools (All Economists)')
    plt.xlabel('Rank Threshold')
    plt.ylabel('Group Size')
    plt.legend()
    plt.grid(True)
    plt.show()

# Load the provided CSV file
data_path = 'dpdp_economics_master_rank.csv'
data_df = pd.read_csv(data_path)

# Run the function for all economists
threshold_var(data_df)

# Filter economists with at least one publication
data_df_filtered = data_df[data_df['NoPPubGrad'] > 0]

# Define threshold for high-status schools
threshold = 50
data_df_filtered['High_Status_School'] = data_df_filtered['RepecRank'] <= threshold

# Perform two-proportion z-test for publications > 1
high_status_group = data_df_filtered[data_df_filtered['High_Status_School']]
low_status_group = data_df_filtered[~data_df_filtered['High_Status_School']]

# Define the success condition (publications > 1)
high_status_success = high_status_group['NoPPubGrad'] > 1
low_status_success = low_status_group['NoPPubGrad'] > 1

# Count successes
high_status_count = high_status_success.sum()
low_status_count = low_status_success.sum()

# Count total observations
high_status_total = len(high_status_group)
low_status_total = len(low_status_group)

# Perform two-proportion z-test
count = np.array([high_status_count, low_status_count])
nobs = np.array([high_status_total, low_status_total])
stat, pval = proportions_ztest(count, nobs)

print(f"High Status Count: {high_status_count}, Total: {high_status_total}")
print(f"Low Status Count: {low_status_count}, Total: {low_status_total}")
print(f"Z-statistic: {stat}, P-value: {pval}")

# Plot the distribution of publication counts for economists with at least one publication
high_status_bins = int(high_status_group['NoPPubGrad'].max())
low_status_bins = int(low_status_group['NoPPubGrad'].max())

plt.figure(figsize=(12, 6))
plt.hist(high_status_group['NoPPubGrad'], bins=range(1, high_status_bins + 2), alpha=0.5, label='High Status', color='g')
plt.hist(low_status_group['NoPPubGrad'], bins=range(1, low_status_bins + 2), alpha=0.5, label='Low Status', color='orange')
plt.title('Distribution of Publication Counts for Economists with at Least One Publication')
plt.xlabel('Number of Publications')
plt.ylabel('Count')
plt.legend()
plt.grid(True)
plt.show()

