import datetime
myname = 'Chaithanya'
myid = 'NCD0818H008'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()

from sys import argv
script, filename, = argv
txt = open(filename)
print "Here's your file again:"
file_again = raw_input("> ")
txt_again = open(file_again)
print txt_again.read()
