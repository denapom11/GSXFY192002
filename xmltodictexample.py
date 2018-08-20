import xmltodict
from pprint import pprint

xml_example = open("xml_example.xml").read()
pprint(xml_example)

xml_dict = xmltodict.parse(xml_example)
pprint(xml_dict)
int_name = xml_dict["interface"]["name"]
print(int_name)
xmlunparsed=xmltodict.unparse(xml_dict)
pprint(xmlunparsed)
