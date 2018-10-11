import datetime
myname = 'MD SABAIR'
myid = 'NCD0318H018'
now = datetime.datetime.now()
from sys import argv
script, filename=argv
txt=open(filename)
print "here is ur file %r" %filename
print txt.read
print "type filename "
file_again =raw_input(">")
txt_again=open(file_again)
print txt_again.read
