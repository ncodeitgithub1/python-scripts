import datetime
myname = 'chandra'
myid = 'NCD0618H003'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
from sys import argv
from os.path import exists

script, from_file, to_file=argv

print "copyinng from %s to %s" % (from_file,to_file)
in_file = open(from_file)
indata = in_file.read()

print "Does the output file exists? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort"
raw_input

out_file = open(to_file, 'w')
out_file.write(indata)


# close both files
out_file.close()
in_file.close()
