import csv

# Opening a CSV file in read mode ('r')
with open('data.csv', 'r') as csv_file:
    # Using csv.reader() to read tabular data from the file
    csv_reader = csv.reader(csv_file)
    
    # Iterating through rows and printing them
    for row in csv_reader:
        print(row)
