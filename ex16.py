import datetime
myname = 'Avinash'
myid = 'NCD0318H022'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()


from sys import argv

script, filename = argv

myfile = open(filename)

print myfile.read()

myfile.close()
