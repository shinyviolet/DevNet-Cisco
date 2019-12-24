#!/usr/bin/env python
"""Working with nested data hands-on exercise / coding challenge."""


import json
import os
from pprint import pprint


# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, "interfaces.json")) as file:
    # TODO: Parse the contents of the JSON file into a variable
    content=json.load(file)
#pprint(content)

# TODO: Loop through the interfaces in the JSON data and print out each
# interface's name, ip, and netmask.
for item in content['ietf-interfaces:interfaces']['interface']:
    print("{}: IP is {}, netmask is{}".format(item['name'],item['ietf-ip:ipv4']['address'][0]['ip'],item['ietf-ip:ipv4']['address'][0]['netmask']))