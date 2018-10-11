import datetime
myname = '<kavya>'
myid = '<NCD0918H006>'
now = datetime.datetime.now()

print" script executed by %s with id %s " % (myname, myid)
print now.isoformat()
from sys import argv
script, filename = argv
print "we are going to earse %r" % filename
print "if you dont want that hit CTRL-C (^C)"
print "if you do want that, hti RETURN"
raw_input("?")
print "opening the file..."
target = open(filename, 'w')
print "truncating the file good bye!"
target.truncate()
print "now i am going to ask you for three lines"
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
print "i am going to write these to the file"
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print "and finally, we close it"
target.close()