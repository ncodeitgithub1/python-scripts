import datetime
myname = 'vasantha'
myid =  'NCD0918H003'
now = datetime.datetime.now()
print " script executed by %s with id %s." % (myname, myid)
print now.isoformat()

from sys import argv
script, filename =  argv
print "we are going to erase %r." % filename
print "If you don't want that. hit CTRL-C(^C)."
print "If you do want that. hit RETURN."
raw_input("?")
print "Opening the file..."
target = open(filename, 'w')
print "truncating the file. Good Bye!"
target.truncate()
print "now I'm going to ask you three lines."
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")
print "I'm going to write these to the file."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print "And finally, we close it."
target.close()

