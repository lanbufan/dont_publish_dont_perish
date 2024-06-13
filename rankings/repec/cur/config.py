"""
"""

# Load the datasets
# year = '2005'
year = '2024'
institutions_path = f'repec_rank_economics_institutions_{year}_with_countries.csv'
# institutions_path = f'repec_rank_economics_institutions_{year}.csv'
# master_path = r'C:\Users\cinep\dpdp\db\dpdp_economics_master_20240608.csv'
# master_path = r'C:\Users\cinep\dpdp\db\dpdp_economics_master_20240612.csv'
master_path = 'dpdp_economics_master_rank_2005.csv'

# Initialize the rank column in professors_df
rank_ = f'Rank_HDSchool_{year}'
rank_cand_ = f'Rank_HDSchool_Cand_{year}'
rank_score_ = f'Rank_HDSchool_Score_{year}'
rank_country_ = f'Rank_HDSchool_Country_{year}'

# Save the result to a new CSV file
output_path = f'dpdp_economics_master_rank_{year}.csv'
