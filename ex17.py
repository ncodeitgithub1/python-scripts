import datetime
myname = 'MD SABAIR'
myid = 'NCD0318H018'
now = datetime.datetime.now()
from sys import argv
from os.path import exists
script, from_file, to_file=argv
print "copying from %s to %s" %(from_file, to_file)
in_file=open(from_file)
indata=in_file.read()
print "the input file is %d bytes long" %len(indata)
print "does the output file exists %r" %exists(to_file)
print "ready hit RETURN to continue, CTRL-C to abort"
raw_input()
out_file=open(to_file,'w')
out_file.write(indata)
print "alryt"
out_file.close()
in_file.close()
