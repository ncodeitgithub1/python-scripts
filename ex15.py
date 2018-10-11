import datetime
myname='sai sadhana'
myid='NCD0418H001'
now= datetime.datetime.now()
print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
from sys import argv
script, filename=argv
txt=open(filename)
print "here is ur file %r" %filename
print txt.read
print "type filename "
file_again =raw_input(">")
txt_again=open(file_again)
print txt_again.read
