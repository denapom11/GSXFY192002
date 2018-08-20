import json
from pprint import pprint

json_example = open("json_example.json").read()
pprint(json_example)

json_python = json.loads(json_example)
pprint(json_python)

int_name = json_python["ietf-interfaces:interface"]["name"]
print(int_name)

pprint(json.dumps(json_python))
