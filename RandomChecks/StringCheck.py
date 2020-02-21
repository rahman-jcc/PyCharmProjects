#!/usr/bin/python

Str = "this is string example....wow!!!";
Str = Str.encode('base64','strict');

suf= "wow!!!";
print "Encoded String: " + Str
print "Decoded String:  " + Str.decode('base64','strict')
print  Str.endswith(suf)

suffix = "wow!!!"
print str.endswith(suffix)
print str.endswith(suffix,20)

suffix = "is"
print str.endswith(suffix, 2, 4)
print str.endswith(suffix, 2, 6)

str = u"this2009"
print str.isnumeric()

str = u"23443434"
print str.isnumeric()

join_str= "Hello"
sequence_str = ["Markus", "Lets", "go"]
print join_str.join (sequence_str)

dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print "dict['Name']: ", dict['Name']