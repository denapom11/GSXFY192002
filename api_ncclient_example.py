
"""
Learning Series: Network Programmability Basics
Module: Programming Fundamentals
Lesson: Python Part 3
Author: Hank Preston <hapresto@cisco.com>

api_ncclient_example.py
Illustrate the following concepts:
- Making NETCONF calls using ncclient library
- Intended to be entered into an interactive
  interpreter
"""

from ncclient import manager
from pprint import pprint
import xmltodict

router = {"ip": "ios-xe-mgmt.cisco.com",
          "port": 10000,
          "user": "root",
          "pass": "D_Vay!_10&"}

netconf_filter = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet1</name>
    </interface>
  </interfaces>
</filter>
"""

m = manager.connect(host=router["ip"],
                    port=router["port"],
                    username=router["user"],
                    password=router["pass"],
                    hostkey_verify=False)

interface_netconf = m.get_config("running", netconf_filter)
pprint(interface_netconf)
interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]
pprint(interface_python)
pprint(interface_python["interfaces"]["interface"]["name"]["#text"])
