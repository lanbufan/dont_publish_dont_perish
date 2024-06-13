import pandas as pd
from fuzzywuzzy import process

from config import *

# Load the datasets
# institutions_path = 'repec_rank_economics_institutions_2024.csv'
# master_path = r'C:\Users\cinep\dpdp\db\dpdp_economics_master_20240608.csv'

# Load the data
institutions_df = pd.read_csv(institutions_path, encoding='latin-1') # utf-8
professors_df = pd.read_csv(master_path)

# Clean column names in institutions_df
institutions_df.columns = institutions_df.columns.str.strip()

# Display the first few rows and the column names to verify
print("Institutions DataFrame Columns:")
print(institutions_df.columns)
print(institutions_df.head())

# Cleaning institution data and keeping the highest rank
institutions_df = institutions_df.sort_values(by='rank').drop_duplicates(subset='university', keep='first')

# Initialize the rank column in professors_df
professors_df[rank_] = None
professors_df[rank_cand_] = None
professors_df[rank_score_] = None
professors_df[rank_country_] = None

# Function to match school names and find the rank and university
def get_rank_and_university(school_name):
    if pd.isna(school_name) or school_name.strip() == '':
        return None, None, None, None
    match = process.extractOne(school_name, institutions_df['university'], score_cutoff=87) # 85 = 6 fp
    if match:
        matched_school = match[0]
        score = match[1]
        row = institutions_df[institutions_df['university'] == matched_school]
        rank = row['rank'].values[0]
        phd_country = row['PhDCountry'].values[0] if 'PhDCountry' in row.columns else None
        return rank, matched_school, score, phd_country
    return None, None, None, None

# Apply the function to each row in professors_df
professors_df[[rank_, rank_cand_, rank_score_, rank_country_]] = professors_df['HDSchool'].apply(lambda x: pd.Series(get_rank_and_university(x)))
# professors_df[[rank_, rank_cand_, rank_score_]] = professors_df['HDSchool'].apply(lambda x: pd.Series(get_rank_and_university(x)))
# professors_df[['Rank_HDSchool_2024', 'Rank_HDSchool_Cand_2024', 'Fuzzy_Score_2024']] = professors_df['HDSchool'].apply(lambda x: pd.Series(get_rank_and_university(x)))
# professors_df[['Rank_HDSchool', 'Rank_HDSchool_Cand']] = professors_df['HDSchool'].apply(lambda x: pd.Series(get_rank_and_university(x)))

# Save the result to a new CSV file
professors_df.to_csv(output_path, index=False)
