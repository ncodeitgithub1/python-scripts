import datetime
myname = '<kavya>'
myid = '<NCD0918H006>'
now = datetime.datetime.now()

print" script executed by %s with id %s " % (myname, myid)
print now.isoformat()
from sys import argv
from os.path import exists
script, from_file, to_file = argv
print "copying from %s to %s" % (from_file, to_file)
in_file = open(from_file)
indata = in_file.read()
print "the input file is %d bytes long" % len(indata)
print "Does the output file exist? %r" % exists(to_file)
print "ready, hit RETURN to continue, CTRL-C to abort"
raw_input()
out_file = open(to_file, 'w')
out_file.write(indata)
print "alright, all done"
out_file.close()
in_file.close()
