import datetime
myname = 'shiva'
myid = 'NCD0518H028'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()


from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)
# read the data from first file
in_file = open(from_file)
indata = in_file.read()


# write it to the second file, if exists
print "Does the output file exists? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort"
raw_input

out_file = open(to_file, 'w')
out_file.write(indata)


# close both files
out_file.close()
in_file.close()

