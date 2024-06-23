"""
#
# Part: Python Math
# API = Application Programming Interface
#
"""

import json

# make a json
x = '{"name": "John", "age": 20, "city": "Phuket"}'

# parse x
y =json.loads(x)

#python Dictionry
print(y)
print(y["city"])

#python Dictionry
a = {
    "name": "John",
    "age": 20,
    "city": "Phuket"
}

# covert into JSON (String)
b = json.dumps(a)

# JSON String
print(b)

