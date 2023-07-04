import pandas as pd

# Read the merged CSV file
df = pd.read_csv('../redd/low_freq/house_1/merged.csv')

# Select the columns representing the devices' watt values
device_columns = df.columns[1:]  # Exclude the first column (timestamp)

# Iterate through each device column
for device_column in device_columns:
    # Find the indices where the watt values are non-zero
    non_zero_indices = df.index[df[device_column] != 0]

    # Check if there are any non-zero values
    if len(non_zero_indices) > 0:
        # Get the start and end indices of the first non-zero values
        start_index = non_zero_indices[0]
        end_index = non_zero_indices[-1]

        # Get the corresponding start and end timestamps
        start_timestamp = df.loc[start_index, 'UNIX_TS']
        end_timestamp = df.loc[end_index, 'UNIX_TS']

        # Find the indices of start_timestamp and end_timestamp
        start_index_timestamp = df.index[df['UNIX_TS'] == start_timestamp].tolist()
        end_index_timestamp = df.index[df['UNIX_TS'] == end_timestamp].tolist()

        print(f"Device: {device_column}")
        print("Start:", start_timestamp, "Index:", start_index_timestamp)
        print("End:", end_timestamp, "Index:", end_index_timestamp)
