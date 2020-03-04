from sklearn.model_selection import train_test_split
import pandas as pd

def clean_data(df):
    df.drop(columns=['Unnamed: 0'], inplace=True)
    # create amount owed columns
    df['amount_owed6'] = df['BILL_AMT6'] - df['PAY_AMT5']
    df['amount_owed5'] = df['BILL_AMT5'] - df['PAY_AMT4']
    df['amount_owed4'] = df['BILL_AMT4'] - df['PAY_AMT3']
    df['amount_owed3'] = df['BILL_AMT3'] - df['PAY_AMT2']
    df['amount_owed2'] = df['BILL_AMT2'] - df['PAY_AMT1']
    # clean education
    df.loc[(df['EDUCATION'] == 0) | (df['EDUCATION'] == 5) | (df['EDUCATION'] == 6), 'EDUCATION'] = 4
    # drop ID column
    df.drop(columns='ID', inplace=True)
    # moved unknown variable to other
    df.MARRIAGE.replace(0.0, 3.0, inplace=True)
    # creates a column of 0

    df['AgeBin'] = 0
    df.loc[((df['AGE'] > 20) & (df['AGE'] < 30)), 'AgeBin'] = 1
    df.loc[((df['AGE'] >= 30) & (df['AGE'] < 40)), 'AgeBin'] = 2
    df.loc[((df['AGE'] >= 40) & (df['AGE'] < 50)), 'AgeBin'] = 3
    df.loc[((df['AGE'] >= 50) & (df['AGE'] < 60)), 'AgeBin'] = 4
    df.loc[((df['AGE'] >= 60) & (df['AGE'] < 70)), 'AgeBin'] = 5
    df.loc[((df['AGE'] >= 70) & (df['AGE'] < 81)), 'AgeBin'] = 6
    # create dummies
    sex_dummies = pd.get_dummies(df['SEX'], prefix='sex', drop_first=True)
    education_dummies = pd.get_dummies(df['EDUCATION'], prefix='edu', drop_first=True)
    marriage_dummies = pd.get_dummies(df['MARRIAGE'], prefix='marriage', drop_first=True)
    age_dummies = pd.get_dummies(df['AgeBin'], prefix='age', drop_first=True)

    df = df.drop(['SEX', 'EDUCATION', 'MARRIAGE', 'AgeBin'], axis=1)
    df = pd.concat([df, sex_dummies], axis=1)
    df = pd.concat([df, education_dummies], axis=1)
    df = pd.concat([df, marriage_dummies], axis=1)
    df = pd.concat([df, age_dummies], axis=1)

    return df.head()
