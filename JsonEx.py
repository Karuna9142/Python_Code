import json

d = {"URL":'https://www.tpointtech.com/','name':'Javatpoint'}
to_json = json.dumps(d)
print(type(to_json))
print(to_json)