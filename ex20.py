import datetime
myname='sai sadhana'
myid='NCD0418H001'
now= datetime.datetime.now()
print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
from sys import argv
script,input_file=argv
def print_all(f):
    print f.read()
def rewind(f):
    f.seek(0)
def print_a_line(line_count,f):
    print line_count,f.readline()
current_file=open(input_file)
print "first letts print the sholw file:\n"
print_all(current_file)
print "now lets rewind, kind of lik tape"
rewind(current_file)
print "lets print 3 lines"
current_line=1
print_a_line(current_line,current_file)
current_a_line=current_line+1
print_a_line(current_line,current_file)
current_a_line=current_line+1
print_a_line(current_line,current_file)
