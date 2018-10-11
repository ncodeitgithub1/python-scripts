import datetime
myname='sai sadhana'
myid='NCD0418H001'
now= datetime.datetime.now()
print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
print "lets practice evrything"
print "you\d need to know \bout escapes with \\ that do \n new lines and \t tabs"
poem="""
\t the lovely word
with logic so firmly planted
cannot discern \n the needs of ove
\n\t\t where there is none
"""
print "---------------"
print poem
print "---------------"
five=10-2+3-6
print "this should be five: %s" %five
def secret_formla(started):
    jelly_beans=started*500
    jars=jelly_beans/1000
    crates=jars/100
    return jelly_beans,jars,crates
start_point=10000
beans,jars,crates=secret_formula(start_point)
print "with startng poimt of %d" %start_point
print "we'd have %d jars, and %d crates" %(beans,jars,crates)
start_point=start_point/10
print "we can also do this way"
print "we have %d beans,%d jars, and %d crates" %secret_formula(start_point)
