import yaml
from pprint import pprint

yml_example = open("yaml_example.yaml").read()
pprint(yml_example)

yaml_python = yaml.load(yml_example)
pprint(yaml_python)

int_name = yaml_python["ietf-interfaces:interface"]["name"]
print(int_name)

pprint(yaml.dump(yaml_python))
