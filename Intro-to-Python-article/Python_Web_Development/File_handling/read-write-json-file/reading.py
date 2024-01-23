import json

# Opening a JSON file in read mode ('r')
with open('data.json', 'r') as json_file:
    # Using json.load() to deserialize and read data from the file
    loaded_data = json.load(json_file)
    print(loaded_data)
