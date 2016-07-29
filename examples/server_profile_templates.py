# -*- coding: utf-8 -*-
###
# (C) Copyright (2012-2016) Hewlett Packard Enterprise Development LP
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
###

from pprint import pprint
from hpOneView.oneview_client import OneViewClient
from config_loader import try_load_from_file

config = {
    "ip": "172.16.102.59",
    "credentials": {
        "userName": "administrator",
        "password": ""
    }
}

# Try load config from a file (if there is a config file)
config = try_load_from_file(config)

oneview_client = OneViewClient(config)

# Get all
print("Get list of all server profile templates")
all_templates = oneview_client.server_profile_templates.get_all()
for template in all_templates:
    print('  %s' % template['name'])

# Get by uri
print("\nGet a server profile template by uri")
template_uri = all_templates[0]["uri"]
template = oneview_client.server_profile_templates.get(template_uri)
pprint(template)

# Get by property
print("\nGet a list of server profile templates that matches the specified macType")
template_mac_type = all_templates[1]["macType"]
templates = oneview_client.server_profile_templates.get_by('macType', template_mac_type)
for template in templates:
    print('  %s' % template['name'])

# Get by name
print("\nGet a server profile templates by name")
template_name = all_templates[0]["name"]
template = oneview_client.server_profile_templates.get_by_name(template_name)
pprint(template)