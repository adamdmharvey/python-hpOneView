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

import os
from pprint import pprint
from hpOneView.oneview_client import OneViewClient

EXAMPLE_CONFIG_FILE = os.path.join(os.path.dirname(__file__), '../config.json')

oneview_client = OneViewClient.from_json_file(EXAMPLE_CONFIG_FILE)

image_streamer_client = oneview_client.create_image_streamer_client()

os_volumes_information = {
    "name": "OSVolume-5",
    "id": "57f2d803-9c11-4f9a-bc02-71804a0fcc3e",
    "archived_id": "123"
}

# Get all OS Volumes
print("\nGet all OS Volumes")
os_volumes = image_streamer_client.os_volumes.get_all()
for os_volume in os_volumes:
    pprint(os_volume)


# Get the OS Volume by ID
print("\nGet the OS Volumes by ID")
os_volume = image_streamer_client.os_volumes.get(os_volumes_information['id'])
pprint(os_volume)


# Get the OS Volume by Name
print("\nGet the OS Volumes by Name")
os_volume = image_streamer_client.os_volumes.get_by_name(os_volumes_information['name'])
pprint(os_volume)
