import datetime
myname = 'Divya bharathi'
myid = 'NCD0318H021'
now = datetime.datetime.now()

print " Script executed by %s with id %s" % (myname, myid)
print now.isoformat()
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "Does the output file exists? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort"
raw_input

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
in_file.close()
