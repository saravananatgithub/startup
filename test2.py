import json
from jsonpath_ng.ext import parse

# Sample JSON data
json_data = '''
[
  {
   "class" : "price",
   "objects" : [
    {
        "name": "Alice",
        "info": {
            "age": 25,
            "cities": ["New York", "Los Angeles"]
        }
    },
    {
        "name": "Bob",
        "info": {
            "age": 30,
            "cities": ["San Francisco", "Chicago"]
        }
    },
    {
        "name": "Charlie",
        "info": {
            "age": 25,
            "cities": ["Boston", "Seattle"]
        }
    }
    
    ]
   }
]
'''

# Load JSON data
data = json.loads(json_data)

# Define jsonpath expression to match key-value pair
jsonpath_expr = parse('$[0].objects[?(@.name == "Bob")].info.age')

# Extract data using jsonpath
matches = [match.value for match in jsonpath_expr.find(data)]

# Print extracted data
print(matches)
