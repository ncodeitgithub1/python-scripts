import datetime

myname = '<ravi teja>'
myid = '<ncd0918h007>'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()

from sys import argv

script, filename = argv

print " we r going to erase %r." % filename
print " if u dont want that, hit CTRL-C (^C)."
print " if u dnt want that, hit return"

raw_input("?")

print " opening the file..."
target = open(filename, 'w')

print "Truncating the file. good bye!"
target.truncate()

print " now im going t ask u 3 lines"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print " im going to write these to the lines"

line1 = raw_input("line1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print " im going to write to these file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
