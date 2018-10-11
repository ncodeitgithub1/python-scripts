import datetime
myname='sai sadhana'
myid='NCD0418H001'
now= datetime.datetime.now()
print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
from sys import argv
script,filename=argv
print "we r goin to erase %r" %filename
print "if u dont want that higt CTRL-C(^C)"
print "if u do want that, hit RETURN"
raw_input("?")
print "opening file"
target=open(filename, 'w')
print "Truncating the file"
target.truncate()
print "now am goin to ask you for 3 lines"
line1=raw_input("line1")
line2=raw_input("line2")
line3=raw_input("line3")
print "am going to arite thses to file"
target.write(line1)
target.write("\n")
