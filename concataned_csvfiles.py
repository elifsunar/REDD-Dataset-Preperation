import csv
import os
import pandas as pd

# Folder path containing the files
folder_path = '../redd/low_freq/house_1'

# Initialize an empty DataFrame to store the merged data
merged_df = pd.DataFrame()

# Initialize a flag to track if any files meet the condition
files_with_desired_length = False

# Iterate over each file in the folder
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)

    if file_name.endswith('.csv'):
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path, header=None)

        # Check the length of the DataFrame
        file_length = len(df)
        print(f"File: {file_name}, Length: {file_length}")

        if file_length == 1561660:
            files_with_desired_length = True
            # Extract the timestamp (first column) and the second column
            timestamp = df.iloc[:, 0]
            second_column = df.iloc[:, 1]

            # Assign the timestamp and the second column to new column names
            timestamp_column_name = 'timestamp'
            second_column_name = os.path.splitext(file_name)[0]

            # Merge the data into the merged DataFrame
            if merged_df.empty:
                merged_df[timestamp_column_name] = timestamp
            merged_df[second_column_name] = second_column

# Save the merged DataFrame as a new CSV file if there are files with the desired length
if files_with_desired_length:
    merged_file_path = os.path.join(folder_path, 'merged_ch1_ch2.csv')
    merged_df.to_csv(merged_file_path, index=False)
    print(f"Merged file saved: {merged_file_path}")
else:
    print("No files with the desired length found.")

