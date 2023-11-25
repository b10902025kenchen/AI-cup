"""
此檔將原本提供之training data以及後來公布public testing data的答案合併成新的training data
讀入2個檔案training.csv與public.csv後，會輸出新的training檔案，名為train.csv
"""
import pandas as pd

# Read the CSV files
public_data = pd.read_csv('training.csv')
private_data = pd.read_csv('public.csv')

# Concatenate the dataframes
combined_data = pd.concat([public_data, private_data], ignore_index=True)

# Write the concatenated data to a new CSV file
combined_data.to_csv('train.csv', index=False)
