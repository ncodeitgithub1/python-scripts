import datetime
myname = '<Venkatesh M>'
myid = '<NCD0518H025>'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()







from sys import argv
script, filename = argv

print "we are going to erase %r" % filename
print "if you dont want , hit CTEL-C (^c)"
print "if you do want that, hit RETURN"

raw_input("?")

print "opening file ..."
target = open (filename, 'w')

print "truncating file. goodbye"
target.truncate()
print "Now i'm going to ask u fro three lines"

line1 =raw_input("line 1")
line2 = raw_input("line 2")
line3 = raw_input("line3")

print "i'm going to write these to file"
target.write(line1)

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "and finally, we close it"
target.close()







