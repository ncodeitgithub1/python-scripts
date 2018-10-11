import datetime
myname = 'vasantha'
myid =  'NCD0918H003'
now = datetime.datetime.now()
print " script executed by %s with id %s." % (myname, myid)
print now.isoformat()

from sys import argv
script, filename =  argv
txt = open(filename)
print "here's your file %r:" % filename
print txt.read()
print "type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)
print txt_again.read()