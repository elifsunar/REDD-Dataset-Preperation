import csv
import os

print("Converting tab-delimited to comma-delimited file...")
outputPath = os.path.dirname('../redd/low_freq/house_1') + 'house1_745878.csv'
with open('../redd/low_freq/house_1/merged.csv') as inputFile:
    with open(outputPath, 'w', newline='') as outputFile:
        reader = csv.reader(inputFile, delimiter=',')
        writer = csv.writer(outputFile, delimiter=' ')

        writer.writerows(reader)

print('Conversion Complete')