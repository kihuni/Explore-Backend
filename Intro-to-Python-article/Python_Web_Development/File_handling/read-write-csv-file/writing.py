import csv

# Creating a list of lists to represent tabular data
data_list = [["Name", "Age", "City"],
             ["Alice", 25, "London"],
             ["Bob", 32, "Paris"]]

# Opening a file in write mode ('w') to store CSV data
with open('data.csv', 'w', newline='') as csv_file:
    # Using csv.writer() to write tabular data to the file
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data_list)
