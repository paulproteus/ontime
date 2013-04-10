#!/usr/bin/python
import os
OUTFILE=os.path.expanduser("~/ontime.jsonlines")

import cgi
form = cgi.FieldStorage()
print 'Content-type: text/plain\r\n'
data = {
    'event': form.getfirst('event', None),
    'supposed_date': form.getfirst('supposed_date', None),
    'supposed_time': form.getfirst('supposed_time', None),
    'notes': form.getfirst('notes', None),
    'ready_time': form.getfirst('ready_time', None),
    }
import json
with open(OUTFILE, 'a') as fd:
    fd.write(json.dumps(data))
print 'OK'
