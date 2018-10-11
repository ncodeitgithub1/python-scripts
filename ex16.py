import datetime

myname = 'SRAVAN'
myid = 'NCD0918H002'
now = datetime.datetime.now()

print " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
from sys import argv
script, filename = argv

print "We are going to erasse %r." % filename
print "If you don't want that, hit CTRL-C(^C)"
print "If you do want that , hit RETURN."

raw_input("?")
print "Operating the file..."
target = open(filename, 'w')
print "Truncating the file. Goodbye!"
target.truncate()
print "Now i'm going yo ask you for three lines."
line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")
print "I'm going to write these to the file ."
target.write(line1)
target.write("\n")