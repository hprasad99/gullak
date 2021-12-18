import json
import re

file_path = 'output.json'
with open(file_path,'r') as f:
    data = json.loads(f.read())
    print(data)

