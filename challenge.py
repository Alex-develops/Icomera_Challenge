import configparser
import json
import time


#Read config.ini file

config = configparser.ConfigParser()
config.read(r"C:\Users\Aleks_Sandra\Desktop\Icomera\config.ini")

#TODO Convert the data from data.txt and part of the data in config.ini to JSON format and save it in a JSON file
#read data from data.txt and save it in a list of dictionaries

presets = config["presets"]
dict1 = {}
data = []
dict1 = dict(config.items("presets"))

with open("data.txt", "r") as f:
    for line in f:
        # Remove parenthesis and form a dict from JSON data
        line_str = '{' + line.strip()[1:-1] + '}'
        line_dict = json.load(line_str)

        data.append(line_dict)

dict1["sentAt"] = time.time()
dict1["dataPoint"] = data

# Create output json file
with open("data.json", "w") as json_file:
    json.dumps(dict1, indent=4)
print(dict1)
