
def get_gender(data_df):

    # Initialize the gender detector
    d = gender.Detector()

    # Define a function to determine gender based on first name
    def get_gender(first_name):
        gender = d.get_gender(first_name)
        if gender in ['unknown', 'andy']:
            return 'Unknown'
        elif gender in ['male', 'mostly_male']:
            return 'Male'
        elif gender in ['female', 'mostly_female']:
            return 'Female'
        else:
            return 'Unknown'

    # Assuming the first name is in a column named 'FirstName'
    data_df['Gender'] = data_df['first_parsed'].apply(lambda x: get_gender(str(x).split()[0]))

    # Check the distribution of the gender variable
    print(data_df['Gender'].value_counts())

    data_df = deal_unknow(data_df)

    # Check the distribution of the gender variable
    print(data_df['Gender'].value_counts())
    print('post_fix')
    dev_log = input()

    return data_df

def deal_unknow(data_df):
    """
    """

    l_unknow = {"Saraswata":"Male",
                "Franque":"Male",
                "Eliav":"Male",
                "Minjie":"Female",
                "Shih":"Male",
                "Wei":"Female",
                "Joao":"Male",
                "Yahong":"Female",
                "Krishna":"Male",
                "Dongwoo":"Male",
                "Xiaoting":"Female",
                "Gorkem":"Male",
                "Li":"Male",
                "Reka":"Female",
                "Vitor":"Male",
                "Hyejin":"Female",
                "Benoit":"Male",
                "Mayssun":"Female",
                "Licun":"Male",
                "Ling":"Female",
                "Amartya":"Male",
                "Dingding":"Female",
                "Yuntong":"Male",
                }

    # Update the 'Gender' column for rows with 'Unknown' gender
    data_df['Gender'] = data_df.apply(lambda row: l_unknow[row['first_parsed']] if row['Gender'] == 'Unknown' and row['first_parsed'] in l_unknow else row['Gender'], axis=1)

    return data_df

def get_ethn(data_df):
    """"
    """
    # Predict ethnicity using the last name
    # data_df = pred_fl_reg_ln(data_df, 'last_parsed')

    # Predict ethnicity using the full name
    data_df = pred_fl_reg_name(data_df, 'first_parsed', 'last_parsed')

    # Display the predictions
    print(data_df[['first_parsed', 'last_parsed', 'race']])

    # Binary
    data_df['RaceBinary'] = data_df['race'].apply(recode_race)

    # Check the distribution of the binary race variable
    print(data_df['RaceBinary'].value_counts())

    return data_df

# Map race to binary: 1 for 'white', 0 for 'non-white'
# Map race to binary: 1 for 'nh_white', 0 for all other races
def recode_race(race):
    return 1 if race == 'nh_white' else 0

# def recode_race(race):
    # if race == 'white':
        # return 1
    # else:
        # return 0

import pandas as pd
import gender_guesser.detector as gender
from ethnicolr import pred_fl_reg_ln, pred_fl_reg_name

if __name__ == "__main__":

    print('should not be run directly')

