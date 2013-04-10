#!/usr/bin/python
import cgi
form = cgi.FieldStorage()
print 'Content-type: text/plain\r\n\r\n'
print form
