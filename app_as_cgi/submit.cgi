#!/usr/bin/python
import cgi
form = cgi.FieldStorage()
print 'Content-type: \r\n\r\n'
print form
