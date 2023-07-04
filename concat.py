import csv
cnt= 0
with open('raw_input2channel_7.csv', encoding='cp850') as file:
    csvreader = csv.reader(file, delimiter=',')
    for row in csvreader:
        for item in row:
            try:
                cnt = cnt+1
                float(item)
                #print(item)
            except ValueError:
                cnt = cnt+1
                print('Non-numeric value:' + str(item) + 'at' + str(cnt))
