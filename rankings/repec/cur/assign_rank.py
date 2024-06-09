import pandas as pd

# Load the provided CSV file
data_path = 'dpdp_economics_master_rank_2024.csv'
data_df = pd.read_csv(data_path)

# Function to calculate the appropriate rank based on HDYear
def calculate_rank(row):
    hd_school = row['HDSchool']
    rank_2005 = row['Rank_HDSchool_2005']
    rank_2024 = row['Rank_HDSchool_2024']

    if pd.isna(hd_school):
        return None

    if pd.notna(rank_2005) and pd.notna(rank_2024):
        if pd.notna(row['HDYear']):
            delta_2005 = abs(row['HDYear'] - 2005)
            delta_2024 = abs(row['HDYear'] - 2024)
            if delta_2005 < delta_2024:
                return rank_2005, "closest_use_2005"
            else:
                return rank_2024, "closest_use_2024"
            # return rank_2005 if delta_2005 < delta_2024 else rank_2024
        else:
            return (rank_2005 + rank_2024) / 2, 'both'
    elif pd.notna(rank_2005):
        return rank_2005, 'closest_use_2005'
    elif pd.notna(rank_2024):
        return rank_2024, 'closest_use_2024'
    else:
        return None, None

# Apply the function to calculate the rank
# data_df['RepecRank', 'RankSource'] = data_df.apply(calculate_rank, axis=1)
# Apply the function to calculate the rank and the usage note
# data_df[['RepecRank', 'RankSource']] = data_df.apply(lambda row: pd.Series(calculate_rank(row)), axis=1)
data_df[['RepecRank', 'RankSource']] = data_df.apply(lambda row: pd.Series(calculate_rank(row), index=['Calculated_Rank', 'Rank_Usage']), axis=1)

# Save the updated dataframe to a new CSV file
output_csv = 'dpdp_economics_master_rank.csv'
data_df.to_csv(output_csv, index=False)
