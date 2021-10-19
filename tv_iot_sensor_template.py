#!/usr/bin/python
# This is a template script which prints metric values of a sensor in JSON format.
# Each metric is described as a variable which gets a random value in between 1 and 20. 

# YOU NEEED TO:

# 1. Upload this script on your device
# 2. Modify this script and assign real values to metric variables - 1.
# 3. Run the script and make sure it prints valid JSON string and nothing else. The JSON should contain all metric value pairs defined within the sensor.
# 4. Set the full path of the script in the sensor configuration page in TeamViewer IoT clould dashboard at http://teamviewer-iot.com/.


from __future__ import print_function

import random
import json

colors_list=["Black","Red","Green","Yellow","Blue","Magenta","Cyan", "White"]
boolean_value_list=[True,False]
data=dict()

data["1"] = random.randint(1,20)


print(json.dumps(data))