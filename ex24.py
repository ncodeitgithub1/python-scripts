import datetime
myname = '<Venkatesh M>'
myid = '<NCD0518H025>'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()






print "lets's practice everything"
print "you\d need to know \ escaping with \\that do \n new lines and \t tabs"
poem= """
\t the lovely world
  enjoy a lot
\n\t\t
"""

print "-------"
print poem
print "--------"
five = 10-2+3-6
print "this should be file %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars =jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars,crates = secret_formula(start_point)
print "we have %d beans, %d jars, and %d crates" % (beans, jars,crates)
start_point = start_point /10
print "we can also do that in way"
print "we have %d beans, %d jars, and %d crates" % secret_formula(start_point)
