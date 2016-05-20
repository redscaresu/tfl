#!/usr/bin/env python

import urllib2
import json

url_api = 'https://api.tfl.gov.uk/line/mode/tube/status'

json_obj = urllib2.urlopen(url_api)

data = json.load(json_obj)
idref = {o['id']: o for o in data}
print idref

