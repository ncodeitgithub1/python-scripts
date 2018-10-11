import datetime
myname = 'SAIKUMAR'
myid = 'NCD0518H024'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()


from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

# read the input file name again from user.
print "Type the filename again:"
file_again = raw_input("> ")

# Open the file for reading
txt_again = open(file_again)

# read the opened file and print it.
print txt_again.read()


