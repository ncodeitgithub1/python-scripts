import datetime
myname = 'chandra'
myid = 'NCD0618H003'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
from sys import argv
script, filename = argv
txt = open(filename)
print "here yor file %r:" % filename
print txt.read()
file.close(txt)
print "type the file name agin"
file_again = raw_input(">")
txt_again = open(file_again)
print txt_again.read()
file.close(txt_again)
