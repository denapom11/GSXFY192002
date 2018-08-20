
"""
Learning Series: Network Programmability Basics
Module: Programming Fundamentals
Lesson: Python Part 3
Author: Hank Preston <hapresto@cisco.com>

api_netmiko_example.py
Illustrate the following concepts:
- Making CLI calls using netmiko library
- Intended to be entered into an interactive
  interpreter
"""
import logging

# Specify to log to a file, specify the format for the message and the date format and the logging level
logging.basicConfig(filename='mylog.log',format='%(asctime)s %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

# Log some messages
logging.debug('This is a debug message. You should see this in the file.')
logging.info('This is an info message. You should see this in the file.')
logging.warning('This is a warning message. You should see this in the file.')



from netmiko import ConnectHandler
from pprint import pprint

try:
    router = {"device_type": "cisco_ios",
              "host": "10.10.20.4",
              "user": "cisco",
              "pass": "cisco_1234!"}

    net_connect = ConnectHandler(ip=router["host"],
                                 username=router["user"],
                                 password=router["pass"],
                                 device_type=router["device_type"])

    interface_cli = net_connect.send_command("show run int Gig1")

    pprint(interface_cli)
    logging.info(interface_cli)
except Exception as e:
    logging.error(e)
