"""
#
# Part: python PIP
#
"""

# pip list
# python.exe -m pip install --upgrade pip]
# pip install camelcase
# pip uninsatll camelcase

import camelcase 
camel = camelcase.CamelCase()
txt = "hello world"
print(camel.hump(txt))
