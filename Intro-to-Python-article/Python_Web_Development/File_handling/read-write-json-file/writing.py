import json

# Creating a Python dictionary to represent data
data = {"name": "John", "age": 30, "city": "New York"}

# Opening a file in write mode ('w') to store JSON data
with open('data.json', 'w') as json_file:
    # Using json.dump() to serialize and write data to the file
    json.dump(data, json_file)