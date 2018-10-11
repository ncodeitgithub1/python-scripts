import datetime
myname = '<Venkatesh M>'
myid = '<NCD0518H025>'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()



myname = 'venkatesh'
myage=25
myheight = 5
myweight = 65
myeyes = 'blue'
myteeth = 'white'
myhair = 'brown'

print "Let's talk about %s "% myname
print "He's %d inches tall" % myheight
print "he;s %d pounds heavy" % myweight

print "actually that's not too heavy"
print "he's got %s eyes and %s hair" % (myeyes, myhair)
print "his teeth are usually %s depending on coffee" % myteeth

print "if i add %d ,%d and %d i get %d " % (myage,myheight,myweight,myage+myheight+myweight)
print "this is %r nothing bew %r in my line of %r work" % (myage,myheight,myweight)
